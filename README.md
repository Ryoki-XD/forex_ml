# 📈 Forex ML Bot — Trading System

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Robot?style=for-the-badge&color=blue)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

O **Forex ML Bot** é uma ferramenta de automação de trading que utiliza modelos de **Machine Learning** para prever movimentos no mercado de moedas. O sistema analisa indicadores técnicos e dados históricos para tomar decisões de entrada e saída de forma inteligente e sem viés emocional.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python (Core do sistema)
* **Data Science:** `Pandas` e `NumPy` para processamento de dados.
* **IA:** `Scikit-Learn` / `XGBoost` para modelagem preditiva.
* **Broker:** `MetaTrader5 API` para execução de ordens em tempo real.

---

## 📂 Estrutura do Projeto

| Arquivo/Pasta | Descrição |
| :--- | :--- |
| `data/` | Bases históricas em CSV/JSON (OHLC). |
| `models/` | Arquivos de modelos treinados (`.pkl` ou `.h5`). |
| `logs/` | Registros detalhados de operações, erros e performance. |
| `main.py` | Ponto de entrada. Executa o loop de trading em tempo real. |
| `train.py` | Script para extração de features e treinamento da IA. |
| `config.py` | Centralização de credenciais e parâmetros de risco. |
| `requirements.txt` | Lista de dependências para o ambiente Python. |

---

## 🔧 Configuração e Instalação

### 1. Requisitos
Certifique-se de ter o **Python 3.8+** instalado e o terminal do **MetaTrader 5** configurado no seu computador.

### 2. Instalação
Clone este repositório e instale as bibliotecas necessárias:

    git clone https://github.com/seu-usuario/forex_ml.git
    cd forex_ml
    pip install -r requirements.txt

### 3. Credenciais
Abra o arquivo `config.py` (ou use um arquivo `.env`) e insira seus dados da corretora:
* **MT5_LOGIN:** Seu número da conta.
* **MT5_PASSWORD:** Sua senha de negociação.
* **MT5_SERVER:** O servidor da sua corretora.

---

## 📈 Como Utilizar

### Passo 1: Treinamento
Para que o bot aprenda com o passado, rode o script de treinamento:

    python train.py

*Isso vai gerar um arquivo na pasta `/models/` que o bot usará para decidir as entradas.*

### Passo 2: Execução
Para colocar o bot para rodar (em modo leitura ou execução):

    python main.py

---

## ⚠️ Aviso Legal (Disclaimer)

> [!IMPORTANT]
> **NEGOCIAR NO MERCADO FOREX ENVOLVE RISCO ALTO.**
> 
> Este software foi desenvolvido para fins de estudo e automação técnica. O desenvolvedor **não se responsabiliza** por quaisquer perdas financeiras. 
> 
> * Nunca opere um capital que você não pode perder.
> * Sempre valide sua estratégia em uma **Conta Demo** por pelo menos 4 semanas antes de usar capital real.

---

## 👨‍💻 Desenvolvedor

**Lucas Diniz de Abreu** *Estudante de Engenharia de Software* [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/lucas-diniz-411705266/)
