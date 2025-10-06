# Aplicativo de Cadastro de Pessoas

Este é um simples aplicativo web para gerenciar um cadastro de pessoas (nome e email), construído com Flask e SQLAlchemy.

## Pré-requisitos

- Python 3.x
- pip (gerenciador de pacotes do Python)

## Instalação

1. **Clone o repositório:**
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_DIRETORIO>
   ```

2. **Crie e ative um ambiente virtual (recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

## Como Executar

1. **Inicie o servidor Flask:**
   ```bash
   python app.py
   ```

2. **Acesse o aplicativo:**
   Abra seu navegador e acesse a seguinte URL:
   ```
   http://127.0.0.1:5000/
   ```

## Funcionalidades

- Adicionar uma nova pessoa com nome e email.
- Visualizar a lista de todas as pessoas cadastradas.
- Os dados são armazenados em um banco de dados SQLite (`pessoas.db`).