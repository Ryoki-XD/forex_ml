# 📈 Forex ML Bot — Trading System

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Robot?style=for-the-badge&color=blue)
![MetaTrader 5](https://img.shields.io/badge/MetaTrader5-Integration-black?style=for-the-badge)

O **Forex ML Bot** é um sistema modular de automação de trading que utiliza **Machine Learning** para prever movimentações no mercado financeiro (foco no par EUR/USD). O bot abrange todo o pipeline de dados: desde a coleta no MetaTrader 5, engenharia de features, treinamento e otimização do modelo, até a execução de ordens em tempo real.

---

## 📂 Arquitetura do Projeto

A estrutura foi desenhada para separar claramente as responsabilidades de Data Science e de Engenharia de Software:

###  Modelagem e Dados
* `coletar_dados.py` — Extrai o histórico de preços (OHLCV) direto do MT5.
* `preparar_dados.py` — Realiza a limpeza e *Feature Engineering* (criação de indicadores técnicos).
* `treinar_modelo.py` — Treina o algoritmo de Machine Learning com a base tratada.
* `otimizar_modelo.py` — Realiza o *Tuning* de hiperparâmetros para buscar a melhor performance.
* `backtester.py` — Valida a estratégia simulando operações no passado.

###  Execução e Conectividade
* `conexao_mt5.py` — Módulo responsável por gerenciar o login e a estabilidade com a corretora.
* `executor_mt5.py` — **[PONTO DE ENTRADA]** O script principal que coloca o bot para rodar em tempo real, lendo os sinais do modelo e enviando ordens.

###  Artefatos
* `*.csv` — Bases de treino, dados brutos e diário de trades.
* `*.pkl` — Modelos já treinados e prontos para uso (ex: `super_cerebro_eurusd_m15.pkl`).

---

## 🔧 Configuração e Instalação

### 1. Pré-requisitos
Certifique-se de ter o **Python 3.8+** instalado e o terminal do **MetaTrader 5** logado na sua conta no mesmo computador.

### 2. Clonando e Preparando o Ambiente
Recomenda-se o uso do ambiente virtual (`venv`) que já está mapeado no projeto.

    git clone https://github.com/seu-usuario/forex_ml.git
    cd forex_ml
    .\venv\Scripts\activate
    pip install -r requirements.txt

### 3. Credenciais
As credenciais da corretora devem ser gerenciadas de forma segura. Certifique-se de configurar o arquivo responsável pela conexão (ajuste no código do `conexao_mt5.py` ou via `.env`, caso utilize).

---

## 🚀 Como Utilizar (Pipeline Completo)

Se você quiser treinar um modelo do zero para um novo ativo ou *timeframe*:

1. **Baixar os dados:**

    python coletar_dados.py

2. **Criar as features e formatar a base:**

    python preparar_dados.py

3. **Treinar e/ou Otimizar:**

    python treinar_modelo.py
    python otimizar_modelo.py

### 🟢 Iniciando as Operações (Live Trading)
Para rodar o bot no mercado ao vivo, utilizando o modelo já salvo:

    python executor_mt5.py

---

## ⚠️ Aviso Legal (Disclaimer)

> [!IMPORTANT]
> **NEGOCIAR NO MERCADO FOREX ENVOLVE ALTO RISCO DE PERDA.**
> 
> Este software foi desenvolvido estritamente para fins acadêmicos e de automação técnica. O desenvolvedor **não se responsabiliza** por quaisquer perdas financeiras. 
> 
> * Nunca opere um capital que você não está disposto a perder.
> * Sempre valide seus próprios modelos (usando o `backtester.py`) e opere inicialmente em uma **Conta Demo**.

---

## 👨‍💻 Desenvolvedor

**Lucas Diniz de Abreu** *Estudante de Engenharia de Software — UniEVANGÉLICA* [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/lucas-diniz-411705266/) 
