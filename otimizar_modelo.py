import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import accuracy_score
import joblib

print("Iniciando o Laboratório de Otimização Genética da IA...")

# 1. Carregando os mesmos dados V2
df = pd.read_csv("dataset_treino_EURUSD.csv")

X = df.drop(columns=['target'])
y = df['target']

# Divisão respeitando a linha do tempo (80% / 20%)
indice_corte = int(len(df) * 0.8)
X_train, X_test = X.iloc[:indice_corte], X.iloc[indice_corte:]
y_train, y_test = y.iloc[:indice_corte], y.iloc[indice_corte:]

# 2. O CARDÁPIO DE CÉREBROS 
parametros = {
    'n_estimators': [100, 200, 300, 500], # Quantidade de árvores
    'max_depth': [5, 7, 10, 15, None],    # Profundidade (Inteligência)
    'min_samples_split': [2, 10, 20],     # Corte de decisões
    'min_samples_leaf': [1, 5, 10]        # Peso das pontas
}

# Criamos o modelo "em branco"
modelo_base = RandomForestClassifier(random_state=42, n_jobs=-1)

# 3. A ARENA DE TESTES
# RandomizedSearchCV vai testar 20 combinações aleatórias desse cardápio
print("⏳ Testando dezenas de cérebros diferentes (Isso vai exigir muito do seu PC, aguarde)...")
otimizador = RandomizedSearchCV(
    estimator=modelo_base, 
    param_distributions=parametros, 
    n_iter=20, # Testa 20 combinações diferentes
    cv=3,      # Faz validação cruzada no tempo
    verbose=2, # Mostra o progresso na tela
    random_state=42, 
    n_jobs=-1  # Usa 100% do seu processador
)

# Inicia a "pancadaria" matemática
otimizador.fit(X_train, y_train)

# 4. OS RESULTADOS
melhor_modelo = otimizador.best_estimator_
previsoes = melhor_modelo.predict(X_test)
nova_acuracia = accuracy_score(y_test, previsoes)

print("\n" + "="*50)
print("🏆 OTIMIZAÇÃO CONCLUÍDA")
print("="*50)
print(f"Antiga Acurácia:  51.39%")
print(f"Nova Acurácia:    {nova_acuracia * 100:.2f}%")
print("-" * 50)
print("🧬 DNA DO NOVO CÉREBRO (Melhores Parâmetros):")
for chave, valor in otimizador.best_params_.items():
    print(f" - {chave}: {valor}")
print("="*50)

# 5. SALVANDO O SUPER CÉREBRO
nome_modelo = "super_cerebro_eurusd_m15.pkl"
joblib.dump(melhor_modelo, nome_modelo)
print(f"\n💾 Novo cérebro salvo como '{nome_modelo}'!")