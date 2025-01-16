PORTUGUESE


```markdown
# Prompt Engineering - Infnet Assessment

## Introdução

Este repositório é dedicado ao projeto de engenharia de prompts, desenvolvido como parte da avaliação do curso de Ciência de dados no Instituto Infnet. O projeto utiliza técnicas avançadas de processamento de linguagem natural para analisar dados legislativos da Câmara dos Deputados do Brasil, visando a automação de insights através de modelos de linguagem de grande escala (LLMs).

## Objetivo do Projeto

O principal objetivo deste projeto é explorar e implementar soluções de engenharia de prompts para automatizar a sumarização de proposições legislativas, análise de sentimentos e extração de insights. Através dessas técnicas, pretendemos oferecer uma ferramenta robusta para o monitoramento e análise das atividades legislativas, proporcionando uma maior transparência e entendimento sobre as decisões políticas no Brasil.

## Estrutura do Repositório

- `dataprep.py`: Este script é responsável pela coleta, preparação e pré-processamento dos dados obtidos através da API da Câmara dos Deputados. Ele trata da autenticação, requisições e organização dos dados em formatos utilizáveis para análises subsequentes.

- `dashboard.py`: Contém o código do dashboard interativo desenvolvido com Streamlit. Este dashboard serve como a interface principal do projeto, onde os usuários podem visualizar análises, sumários e diversos insights sobre as atividades da Câmara.

- `data/`: Diretório que armazena os dados processados, sumários gerados e outros artefatos de dados necessários para o funcionamento do dashboard.

- `models/`: Pasta que inclui modelos de machine learning treinados e outros recursos de modelagem necessários para a análise de dados.

- `.env`: Um arquivo crucial que armazena variáveis de ambiente necessárias para a operação segura do projeto, como chaves de API. Este arquivo não é rastreado pelo Git para proteger informações sensíveis.

## Configuração e Execução

### Pré-requisitos

Para executar este projeto, você precisará de Python 3.8 ou superior e pip para gerenciamento de dependências. É recomendável criar um ambiente virtual Python para evitar conflitos de dependências.

### Instalação

Clone o repositório para sua máquina local e instale as dependências necessárias:

```bash
git clone https://github.com/danimoreira90/Prompt-Engineering---Infnet-Assessment.git
cd Prompt-Engineering---Infnet-Assessment
pip install -r requirements.txt
```

### Configuração

Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis de ambiente:

```plaintext
GEMINI_API_KEY=your_gemini_api_key_here
```

Substitua `your_gemini_api_key_here` pela sua chave de API real.

### Executando o Dashboard

Para iniciar o dashboard, execute o seguinte comando no terminal:

```bash
streamlit run dashboard.py
```

Acesse o dashboard pelo navegador em `http://localhost:8501`.

## Contribuições

Contribuições são bem-vindas e incentivadas. Se você deseja melhorar o código ou as funcionalidades do projeto, siga este processo:

1. Fork o repositório.
2. Crie uma nova branch (`git checkout -b feature/NovaFuncionalidade`).
3. Faça suas alterações.
4. Commit suas mudanças (`git commit -am 'Adiciona alguma funcionalidade'`).
5. Push para a branch (`git push origin feature/NovaFuncionalidade`).
6. Abra um Pull Request.


## Contato

Dúvidas ou sugestões podem ser encaminhadas através do [tracker de issues](https://github.com/danimoreira90/Prompt-Engineering---Infnet-Assessment/issues) do GitHub ou pelo contato direto via e-mail disponível no perfil do repositório.
```


ENGLISH

```markdown
# Prompt Engineering - Infnet Assessment

## Introduction

This repository is dedicated to the prompt engineering project, developed as part of the Information Technology course assessment at Infnet. The project utilizes advanced natural language processing techniques to analyze legislative data from the Brazilian Chamber of Deputies, aiming to automate insights through Large Language Models (LLMs).

## Project Objective

The main goal of this project is to explore and implement prompt engineering solutions to automate the summarization of legislative propositions, sentiment analysis, and insight extraction. Through these techniques, we aim to provide a robust tool for monitoring and analyzing legislative activities, offering greater transparency and understanding of political decisions in Brazil.

## Repository Structure

- `dataprep.py`: This script is responsible for collecting, preparing, and pre-processing data obtained via the Chamber of Deputies' API. It handles authentication, requests, and organizes the data into usable formats for subsequent analyses.

- `dashboard.py`: Contains the code for the interactive dashboard developed with Streamlit. This dashboard serves as the main interface of the project, where users can view analyses, summaries, and various insights about the Chamber's activities.

- `data/`: Directory that stores processed data, generated summaries, and other data artifacts necessary for the dashboard's operation.

- `models/`: Folder that includes trained machine learning models and other modeling resources needed for data analysis.

- `.env`: A crucial file that stores environment variables necessary for the secure operation of the project, such as API keys. This file is not tracked by Git to protect sensitive information.

## Setup and Execution

### Prerequisites

To run this project, you will need Python 3.8 or higher and pip for dependency management. It is recommended to create a Python virtual environment to avoid dependency conflicts.

### Installation

Clone the repository to your local machine and install the necessary dependencies:

```bash
git clone https://github.com/danimoreira90/Prompt-Engineering---Infnet-Assessment.git
cd Prompt-Engineering---Infnet-Assessment
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the root of the project and add the following environment variables:

```plaintext
GEMINI_API_KEY=your_gemini_api_key_here
```

Replace `your_gemini_api_key_here` with your actual API key.

### Running the Dashboard

To start the dashboard, execute the following command in the terminal:

```bash
streamlit run dashboard.py
```

Access the dashboard through the browser at `http://localhost:8501`.

## Contributions

Contributions are welcome and encouraged. If you wish to improve the code or functionalities of the project, follow this process:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/NewFeature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature/NewFeature`).
6. Open a Pull Request.


## Contact

Questions or suggestions can be directed through the [issue tracker](https://github.com/danimoreira90/Prompt-Engineering---Infnet-Assessment/issues) on GitHub or direct contact via email available on the repository profile.
```
