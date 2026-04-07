import pandas as pd
import joblib
import matplotlib.pyplot as plt

print("Construindo a Máquina do Tempo Quantitativa...")

# 1. CARREGANDO DADOS E O CÉREBRO
try:
    df = pd.read_csv("dataset_treino_EURUSD.csv")
    modelo = joblib.load("super_cerebro_eurusd_m15.pkl")
    print("✅ Dados e Cérebro V2 carregados.")
except Exception as e:
    print("❌ Erro ao carregar arquivos. Verifique se estão na pasta.")
    quit()

# 2. SEPARANDO O "FUTURO" 
indice_corte = int(len(df) * 0.8)
df_teste = df.iloc[indice_corte:].copy()

X_test = df_teste.drop(columns=['target'])
y_test = df_teste['target']

print(f"🔄 Simulando {len(X_test)} operações no histórico invisível...")

# 3. FAZENDO AS PREVISÕES DO PASSADO
previsoes = modelo.predict(X_test)

# 4. A SIMULAÇÃO FINANCEIRA (Gestão de Risco 1:3)
CAPITAL_INICIAL = 10000.00
RISCO_POR_TRADE = 10.00   # Stop Loss (10 dólares)
RETORNO_POR_TRADE = 30.00 # Take Profit (30 dólares)

capital_atual = CAPITAL_INICIAL
evolucao_capital = [] # Lista para guardar a curva de dinheiro
trades_vencedores = 0
trades_perdedores = 0

for i in range(len(previsoes)):
    previsao_ia = previsoes[i]
    resultado_real = y_test.iloc[i]
    
    # Se a IA acertou a direção
    if previsao_ia == resultado_real:
        capital_atual += RETORNO_POR_TRADE
        trades_vencedores += 1
    # Se a IA errou a direção
    else:
        capital_atual -= RISCO_POR_TRADE
        trades_perdedores += 1
        
    # Salva o capital após a operação para desenhar o gráfico
    evolucao_capital.append(capital_atual)

# 5. OS RESULTADOS
lucro_liquido = capital_atual - CAPITAL_INICIAL
taxa_acerto = (trades_vencedores / len(previsoes)) * 100

print("\n" + "="*40)
print("📈 RESULTADO DO BACKTEST (10.000 Trades)")
print("="*40)
print(f"Capital Inicial:  ${CAPITAL_INICIAL:,.2f}")
print(f"Capital Final:    ${capital_atual:,.2f}")
print(f"Lucro Líquido:    ${lucro_liquido:,.2f}")
print("-" * 40)
print(f"Trades Certos:    {trades_vencedores}")
print(f"Trades Errados:   {trades_perdedores}")
print(f"Taxa de Acerto:   {taxa_acerto:.2f}%")
print("="*40)

# 6. DESENHANDO O GRÁFICO 
plt.figure(figsize=(10, 5))
plt.plot(evolucao_capital, color='blue', linewidth=1.5)
plt.title('Curva de Patrimônio (Equity Curve) - IA EURUSD V2')
plt.xlabel('Número de Operações')
plt.ylabel('Saldo em Dólares ($)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.axhline(y=CAPITAL_INICIAL, color='red', linestyle='-', alpha=0.5, label='Capital Inicial')
plt.legend()
plt.tight_layout()

print("📊 Gerando o gráfico... (Feche a janela do gráfico para encerrar o script)")
plt.show()