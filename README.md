# Credit Card Validation Project

Este é um projeto desenvolvido como parte de um desafio do Bootcamp de Inteligência Artificial, utilizando **Streamlit**, **Azure Blob Storage** e a API **Binlist.net** para validação de cartões de crédito.

## Funcionalidades

- Upload de imagens de cartões de crédito.
- Validação de números de cartões de crédito usando o Algoritmo de Luhn.
- Identificação de informações do cartão (banco, esquema, país) usando a API Binlist.
- Integração com o Azure Blob Storage para armazenamento de imagens.

## Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas:

- Python 3.9 ou superior
- Conta no [Azure Blob Storage](https://azure.microsoft.com/)
- Biblioteca `binlist.net` configurada

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/leonardoeng13/credit-card-validation.git
   cd credit-card-validation

2. Crie e ative um ambiente virtual:
   ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use venv\Scripts\activate

3. Instale as dependências:
   ```bash
    pip install -r requirements.txt

4. Configure o arquivo .env: Crie um arquivo .env baseado no .env.example e preencha as credenciais do Azure.

## Uso

Execute o aplicativo com:
    ```bash
    streamlit run src/app.py
    Acesse o Streamlit no navegador em http://localhost:8501 para fazer upload e validar cartões de crédito.

## Contribuições
Sinta-se à vontade para abrir Issues e Pull Requests para melhorias.

## Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
