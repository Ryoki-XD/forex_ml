import pandas as pd
import numpy as np

print("Carregando arquivo CSV bruto...")
df = pd.read_csv("historico_EURUSD_M15.csv")
df['time'] = pd.to_datetime(df['time'])

print("Calculando features matemáticas Avançadas (V2.0)...")

# --- FEATURES CLÁSSICAS ---
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

# --- NOVAS FEATURES ---

# 1. RSI (Índice de Força Relativa - 14 períodos)
delta = df['close'].diff()
gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
rs = gain / loss
df['rsi_14'] = 100 - (100 / (1 + rs))

# 2. MACD (Convergência/Divergência de Médias Móveis)
ema_12 = df['close'].ewm(span=12, adjust=False).mean()
ema_26 = df['close'].ewm(span=26, adjust=False).mean()
df['macd'] = ema_12 - ema_26
df['macd_signal'] = df['macd'].ewm(span=9, adjust=False).mean()
df['macd_hist'] = df['macd'] - df['macd_signal'] # O histograma do MACD

# 3. Bandas de Bollinger (20 períodos, 2 desvios padrões)
df['bb_middle'] = df['close'].rolling(window=20).mean()
std_20 = df['close'].rolling(window=20).std()
df['bb_upper'] = df['bb_middle'] + (std_20 * 2)
df['bb_lower'] = df['bb_middle'] - (std_20 * 2)
# Distância do preço atual para as bandas superior e inferior
df['dist_bb_upper'] = df['close'] - df['bb_upper']
df['dist_bb_lower'] = df['close'] - df['bb_lower']

# --- O ALVO ---
df['target_price'] = df['close'].shift(-3)
df['target'] = np.where(df['target_price'] > df['close'], 1, 0)

# Limpeza dos valores vazios criados pelas médias
df.dropna(inplace=True)

# Removemos colunas que a IA não deve ver 
colunas_para_remover = ['time', 'open', 'high', 'low', 'close', 'real_volume', 'target_price']
features = df.drop(columns=colunas_para_remover)

nome_arquivo_treino = "dataset_treino_EURUSD.csv"
features.to_csv(nome_arquivo_treino, index=False)

print(f"✅ Sucesso! Dataset V2 preparado com {len(features)} exemplos.")
print(f"🧠 Agora temos {len(features.columns) - 1} indicadores alimentando o modelo.")