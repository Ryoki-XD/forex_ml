import MetaTrader5 as mt5
import pandas as pd
import joblib
import time
import csv
import os
from datetime import datetime

# --- CONFIGURAÇÕES DO ROBÔ ---
SIMBOLO = "EURUSD"
LOTE = 0.10
STOP_LOSS_PONTOS = 150
TAKE_PROFIT_PONTOS = 450
MAGIC_NUMBER = 1001
ARQUIVO_LOG = "diario_de_trades.csv"

print("Iniciando Robô Autônomo M15 (Versão 2.0 com MACD/RSI/BB)...")

try:
    modelo = joblib.load("super_cerebro_eurusd_m15.pkl")
    print("🧠 Cérebro V2 carregado!")
except Exception as e:
    print("❌ Erro ao carregar o modelo.")
    quit()

if not mt5.initialize():
    print("❌ Falha na inicialização do MT5.")
    quit()

def registrar_trade(direcao, preco, sl, tp, ticket):
    cabecalho = ["data_hora", "ativo", "direcao", "preco_entrada", "stop_loss", "take_profit", "ticket"]
    existe = os.path.isfile(ARQUIVO_LOG)
    with open(ARQUIVO_LOG, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not existe:
            writer.writerow(cabecalho)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), SIMBOLO, direcao, preco, sl, tp, ticket])
        print("📝 Operação gravada no Diário!")

def executar_analise_e_trade():
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Acordando para analisar {SIMBOLO}...")
    
    posicoes = mt5.positions_get(symbol=SIMBOLO)
    if posicoes is None: return
    elif len(posicoes) > 0:
        print("⏳ Operação em andamento. Aguardando...")
        return

    # Puxamos 100 velas agora para o MACD e médias longas terem base
    rates = mt5.copy_rates_from_pos(SIMBOLO, mt5.TIMEFRAME_M15, 0, 100)
    df = pd.DataFrame(rates)
    
    # --- CÁLCULO DE FEATURES ---
    df['body_size'] = df['close'] - df['open']
    df['return_1'] = df['close'].pct_change()
    df['return_2'] = df['close'].pct_change(periods=2)
    df['return_3'] = df['close'].pct_change(periods=3)
    df['volatility_10'] = df['return_1'].rolling(window=10).std()
    df['volatility_20'] = df['return_1'].rolling(window=20).std()
    df['sma_10'] = df['close'].rolling(window=10).mean()
    df['sma_50'] = df['close'].rolling(window=50).mean()
    df['dist_sma_10'] = df['close'] - df['sma_10']
    df['momentum_5'] = df['close'] - df['close'].shift(5)

    # RSI
    delta = df['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['rsi_14'] = 100 - (100 / (1 + rs))

    # MACD
    ema_12 = df['close'].ewm(span=12, adjust=False).mean()
    ema_26 = df['close'].ewm(span=26, adjust=False).mean()
    df['macd'] = ema_12 - ema_26
    df['macd_signal'] = df['macd'].ewm(span=9, adjust=False).mean()
    df['macd_hist'] = df['macd'] - df['macd_signal']

    # Bollinger Bands
    df['bb_middle'] = df['close'].rolling(window=20).mean()
    std_20 = df['close'].rolling(window=20).std()
    df['bb_upper'] = df['bb_middle'] + (std_20 * 2)
    df['bb_lower'] = df['bb_middle'] - (std_20 * 2)
    df['dist_bb_upper'] = df['close'] - df['bb_upper']
    df['dist_bb_lower'] = df['close'] - df['bb_lower']
    
    df.dropna(inplace=True)
    
    # As exatas 21 colunas que a IA treinou
    colunas_features = [
        'tick_volume', 'spread', 'body_size', 'return_1', 'return_2', 'return_3', 
        'volatility_10', 'volatility_20', 'sma_10', 'sma_50', 'dist_sma_10', 'momentum_5',
        'rsi_14', 'macd', 'macd_signal', 'macd_hist', 'bb_middle', 'bb_upper', 
        'bb_lower', 'dist_bb_upper', 'dist_bb_lower'
    ]
    
    estado_atual = df[colunas_features].iloc[-1:]

    # PREVISÃO
    previsao = modelo.predict(estado_atual)[0]
    tick = mt5.symbol_info_tick(SIMBOLO)
    point = mt5.symbol_info(SIMBOLO).point

    if previsao == 1:
        direcao = "COMPRA"
        tipo_ordem = mt5.ORDER_TYPE_BUY
        preco = tick.ask
        sl = preco - (STOP_LOSS_PONTOS * point)
        tp = preco + (TAKE_PROFIT_PONTOS * point)
    else:
        direcao = "VENDA"
        tipo_ordem = mt5.ORDER_TYPE_SELL
        preco = tick.bid
        sl = preco + (STOP_LOSS_PONTOS * point)
        tp = preco - (TAKE_PROFIT_PONTOS * point)

    print(f"🤖 IA decidiu: {direcao}!")

    requisicao = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": SIMBOLO,
        "volume": LOTE,
        "type": tipo_ordem,
        "price": preco,
        "sl": sl,
        "tp": tp,
        "deviation": 20,
        "magic": MAGIC_NUMBER,
        "comment": "Forex-IA-Bot-V2",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_FOK,
    }

    res = mt5.order_send(requisicao)
    if res.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"❌ Erro ao enviar ordem: {res.retcode}")
    else:
        print(f"✅ Ordem {direcao} aberta em {preco:.5f}")
        registrar_trade(direcao, preco, sl, tp, res.order)

# --- LOOP PRINCIPAL ---
try:
    while True:
        agora = datetime.now()
        if agora.minute % 15 == 0 and agora.second < 10:
            executar_analise_e_trade()
            time.sleep(60) 
        else:
            time.sleep(5)
except KeyboardInterrupt:
    print("\n🛑 Robô desligado pelo usuário.")
    mt5.shutdown()