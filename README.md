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


---

## English Version

# Credit Card Validation

This project was developed as part of an Artificial Intelligence Bootcamp challenge, using **Streamlit**, **Azure Blob Storage**, and the **Binlist.net** API to validate credit cards.

## Features

- Upload credit card images.
- Validate credit card numbers using the Luhn Algorithm.
- Identify card information (bank, scheme, country) using the Binlist API.
- Integration with Azure Blob Storage for image storage.

## Prerequisites

Make sure you have the following tools installed:

- Python 3.9 or later
- An account on [Azure Blob Storage](https://azure.microsoft.com/)
- `binlist.net` API properly configured

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/leonardoeng13/credit-card-validation.git
   cd credit-card-validation

2. Create and activate a virtual environment:
   ```bash
    Copiar código
    python -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate

3. Install the dependencies:
   ```bash
    Copiar código
    pip install -r requirements.txt

4. Configure the .env file:
Create a .env file based on .env.example and fill in the Azure credentials and Binlist API URL.

## Usage

Run the application with:
    ```bash
    streamlit run src/app.py

Access Streamlit in your browser at http://localhost:8501 to upload and validate credit cards.

## Contributions
Feel free to open Issues and Pull Requests for improvements.

## License
This project is licensed under the MIT license. See the LICENSE file for more details.
