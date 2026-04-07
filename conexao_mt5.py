import MetaTrader5 as mt5

# Estabelece a conexão com o terminal MetaTrader 5
print("\nTentando conectar ao MetaTrader 5...")

# O initialize() procura o MT5 aberto no seu computador e se conecta a ele
if not mt5.initialize():
    print("❌ Falha ao inicializar o MetaTrader5. Erro:", mt5.last_error())
    quit()

print("✅ Conectado com sucesso ao MT5!\n")

# Coleta informações da conta (Para provar que estamos lendo os dados reais)
account_info = mt5.account_info()
if account_info != None:
    print("=== DADOS DA SUA CONTA DEMO ===")
    print(f"Número da Conta: {account_info.login}")
    print(f"Corretora: {account_info.company}")
    print(f"Saldo Fictício: ${account_info.balance}")
    print(f"Alavancagem: 1:{account_info.leverage}")
else:
    print("❌ Não foi possível puxar os dados da conta. Erro:", mt5.last_error())

# Fecha a conexão para não deixar processo pendurado
mt5.shutdown()