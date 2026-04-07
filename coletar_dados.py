import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime

# Configurações do ativo que vamos baixar
SIMBOLO = "EURUSD"
TIMEFRAME = mt5.TIMEFRAME_M15  # Velas de 15 minutos
QTD_VELAS = 50000              # Quantidade de velas históricas

print(f"Iniciando conexão com MT5 para baixar {QTD_VELAS} velas de {SIMBOLO}...")

if not mt5.initialize():
    print("❌ Falha na inicialização do MT5. Erro:", mt5.last_error())
    quit()

# Pede ao terminal os dados históricos
print("Baixando dados... Isso pode levar alguns segundos.")
rates = mt5.copy_rates_from_pos(SIMBOLO, TIMEFRAME, 0, QTD_VELAS)

mt5.shutdown()

# Verifica se os dados vieram
if rates is None or len(rates) == 0:
    print(f"❌ Erro ao baixar dados. O símbolo {SIMBOLO} está disponível na sua conta?")
else:
    # Transforma os dados brutos em uma tabela bonitinha do Pandas (DataFrame)
    df = pd.DataFrame(rates)
    
    # Converte a coluna 'time' (que vem em segundos) para formato de data e hora real
    df['time'] = pd.to_datetime(df['time'], unit='s')
    
    # Salva os dados em um arquivo CSV na sua pasta
    nome_arquivo = f"historico_{SIMBOLO}_M15.csv"
    df.to_csv(nome_arquivo, index=False)
    
    print(f"✅ Sucesso! Foram baixadas {len(df)} linhas.")
    print(f"Primeira data: {df['time'].iloc[0]}")
    print(f"Última data: {df['time'].iloc[-1]}")
    print(f"Arquivo salvo como: {nome_arquivo}")