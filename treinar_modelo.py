import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

print("Carregando o dataset preparado...")
df = pd.read_csv("dataset_treino_EURUSD.csv")

# Separa as 'Features' (Indicadores) do 'Target' (A Resposta: 1 para Subiu, 0 para Caiu)
X = df.drop(columns=['target'])
y = df['target']

# DIVISÃO NO TEMPO (80% Treino, 20% Teste)
# a linha do tempo deve ser respeitada!
indice_corte = int(len(df) * 0.8)

X_train, X_test = X.iloc[:indice_corte], X.iloc[indice_corte:]
y_train, y_test = y.iloc[:indice_corte], y.iloc[indice_corte:]

print(f"📚 IA estudando {len(X_train)} velas de passado...")
print(f"📝 IA fará a prova em {len(X_test)} velas de 'futuro'...")

# 1. CRIANDO A IA (Random Forest / Floresta Aleatória)
# max_depth=5 evita que a IA 'decore' os dados (Overfitting) e force ela a aprender os padrões reais
modelo = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42, n_jobs=-1)

print("\nTreinando a Floresta Aleatória (Isso pode levar alguns segundos)...")
modelo.fit(X_train, y_train)

# 2. APLICANDO A PROVA SURPRESA
print("Fazendo previsões nos dados de teste...")
previsoes = modelo.predict(X_test)

# 3. CORRIGINDO A PROVA
acuracia = accuracy_score(y_test, previsoes)
print(f"\n================ RESULTADO ==================")
print(f"🎯 Acurácia Geral: {acuracia * 100:.2f}%")
print("=============================================\n")

# Mostra onde ela é boa (Prever quedas = 0, Prever altas = 1)
print(classification_report(y_test, previsoes))

# 4. SALVANDO O CÉREBRO
nome_modelo = "cerebro_eurusd_m15.pkl"
joblib.dump(modelo, nome_modelo)
print(f"🧠 Cérebro treinado e salvo com sucesso como '{nome_modelo}'!")