============================================================
                FOREX ML BOT - TRADING SYSTEM
============================================================

DESENVOLVEDOR: Lucas Diniz de Abreu
VERSÃO: 1.0
LINGUAGEM: Python 3.x

------------------------------------------------------------
1. DESCRIÇÃO
------------------------------------------------------------
O Forex ML Bot é uma ferramenta de automação de trading que 
utiliza modelos de Machine Learning para prever movimentos 
no mercado de moedas. O sistema analisa indicadores técnicos 
e dados históricos para tomar decisões de entrada e saída.

------------------------------------------------------------
2. TECNOLOGIAS UTILIZADAS
------------------------------------------------------------
- Python (Core do sistema)
- Pandas/NumPy (Processamento de dados)
- Scikit-Learn/XGBoost (Modelagem preditiva)
- MetaTrader5 API (Execução de ordens)

------------------------------------------------------------
3. ESTRUTURA DO PROJETO
------------------------------------------------------------
/data        - Bases históricas em CSV/JSON
/models      - Arquivos de modelos treinados (.pkl)
/logs        - Registros de operações e erros
main.py      - Script principal de execução
train.py     - Script para treinamento do modelo
config.py    - Configurações de API e parâmetros de risco
requirements.txt - Dependências do projeto

------------------------------------------------------------
4. COMO INSTALAR
------------------------------------------------------------
1. Certifique-se de ter o Python 3.8+ instalado.
2. Instale as bibliotecas necessárias:
   $ pip install -r requirements.txt

3. Configure suas credenciais no arquivo .env ou config.py:
   - Login da Corretora
   - Senha
   - Servidor

------------------------------------------------------------
5. COMO UTILIZAR
------------------------------------------------------------
Para treinar o modelo com dados novos:
$ python train.py

Para iniciar o bot em modo de monitoramento/execução:
$ python main.py

------------------------------------------------------------
6. AVISO LEGAL (DISCLAIMER)
------------------------------------------------------------
O investimento em Forex envolve riscos elevados. Este bot é 
uma ferramenta de estudo e suporte. O desenvolvedor não se 
responsabiliza por quaisquer perdas financeiras resultantes 
do uso deste software em contas reais. 

TESTE SEMPRE EM CONTA DEMO.
------------------------------------------------------------
============================================================