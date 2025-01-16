import streamlit as st
import pandas as pd
import plotly.express as px
import yaml
import re
import matplotlib.pyplot as plt
from PIL import Image
import json

# Carregando os dados
proposicoes = pd.read_parquet(r"D:\Pastas\Infnet\Infnet - 2024.2\Engenharia de Prompts\AT\data\proposicoes_deputados.parquet")
despesas = pd.read_parquet(r"D:\Pastas\Infnet\Infnet - 2024.2\Engenharia de Prompts\AT\data\serie_despesas_diárias_deputados.parquet")
caminho_json = r"D:\Pastas\Infnet\Infnet - 2024.2\Engenharia de Prompts\AT\data\insights_distribuicao_deputados.json"


st.set_page_config(page_title="Análise de Dados da Câmara dos Deputados", layout="wide")

# Aba Overview
st.sidebar.title("Navegação")
page = st.sidebar.radio("Selecione uma aba:", ('Overview', 'Despesas', 'Proposições'))

if page == 'Overview':
    st.title("Análise de Dados da Câmara dos Deputados")
    st.markdown("""
    Este projeto visa analisar dados da Câmara dos Deputados, fornecendo insights sobre as despesas parlamentares e as proposições legislativas.  
    A Câmara dos Deputados é composta por 513 deputados, eleitos por representação proporcional para mandatos de quatro anos.  
    Suas funções incluem legislar, representar o povo e fiscalizar o governo.

    **Nesta aplicação, você encontrará:**

    * **Despesas:** Visualizações de dados sobre os gastos dos deputados.
    * **Proposições:** Resumos de proposições relevantes.

    **Links Importantes:**

    * [Câmara dos Deputados](https://www.camara.leg.br/)
    """)


# Aba Despesas
elif page == 'Despesas':
    st.title("Análise de Despesas Parlamentares")

    # Pré-processamento (simplificado para exemplo) - Adaptar conforme necessário
    despesas_agregadas = despesas.groupby('deputado_nome')['valor_despesa'].sum().reset_index()
    despesas_agregadas = despesas_agregadas.sort_values('valor_despesa', ascending=False)


    st.subheader("Top 10 Deputados com Maiores Despesas")
    fig_despesas = px.bar(despesas_agregadas.head(10), x='deputado_nome', y='valor_despesa', title='Top 10 Deputados com Maiores Despesas')
    st.plotly_chart(fig_despesas)

    st.subheader("Distribuição das Despesas")
    fig_dist = px.histogram(despesas, x='valor_despesa', title='Distribuição das Despesas')
    st.plotly_chart(fig_dist)


# Aba Proposições
elif page == 'Proposições':
    st.title("Análise de Proposições")

    # Pré-processamento (simplificado para exemplo) - Adaptar conforme necessário
    temas = ['Economia', 'Educação', 'Ciência']
    proposicoes_filtradas = proposicoes[proposicoes['Tema'].isin(temas)].head(10)

    for index, row in proposicoes_filtradas.iterrows():
        st.subheader(row['uri'])
        st.markdown(f"**Tema:** {row['Tema']}")
        st.markdown(f"**Resumo:** {row['ementa']}") # Substituir por um resumo mais elaborado se necessário.
        st.markdown("---")

def fix_encoding(text):
    text = text.replace('Ã¢', 'â')
    text = text.replace('Ã£', 'ã')
    text = text.replace('Ã³', 'ó')
    text = text.replace('Ã§', 'ç')
    text = text.replace('Ã¼', 'ü')
    text = re.sub(r'Ã\w+', lambda m: m.group(0).replace('Ã', ''), text) #catch other possibilities

    return text


try:
    with open('./data/config.yaml', 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
        overview_summary = config['overview_summary']
        overview_summary = fix_encoding(overview_summary)

except FileNotFoundError:
    overview_summary = "Arquivo config.yaml não encontrado."
except KeyError:
    overview_summary = "Chave 'overview_summary' não encontrada no arquivo config.yaml."
except yaml.YAMLError as e:
    overview_summary = f"Erro ao ler o arquivo YAML: {e}"


st.title('Dashboard - Câmara dos Deputados (ago/2024)')
st.markdown(overview_summary)

def overview_page():
    st.title("Overview")

    # Texto resumido (assumindo que este código já existe de response2)
    st.write("Aqui vai um texto resumido sobre os dados da Câmara dos Deputados.  Este texto descreve brevemente o conteúdo dos datasets utilizados, destacando as informações chave disponíveis para análise.")


    # Carregando e exibindo a imagem
    try:
        img = Image.open(r"D:\Pastas\Infnet\Infnet - 2024.2\Engenharia de Prompts\AT\data\distribuicao_deputados.png")
        st.markdown("<h3 style='text-align: center;'>Distribuição dos Deputados</h3>", unsafe_allow_html=True)
        st.image(img, use_container_width=True)
    except FileNotFoundError:
        st.error("Imagem 'distribuicao_deputados.png' não encontrada. Certifique-se de que o caminho está correto.")


def proposicoes_page():
    st.title("Proposições")
    # Código para análise e visualização das proposições (de response1 ou response2)
    st.write("Análise de proposições")


def despesas_page():
    st.title("Despesas")
    # Código para análise e visualização das despesas (de response1 ou response2)
    st.write("Aqui seria a análise de despesas")

def carregar_insights(caminho_json):
    try:
        with open(caminho_json, 'r') as f:
            dados = json.load(f)
            return dados['insights']
    except FileNotFoundError:
        st.error(f"Arquivo JSON não encontrado em: {caminho_json}")
        return None
    except KeyError:
        st.error(f"Chave 'insights' não encontrada no arquivo JSON: {caminho_json}")
        return None


# Streamlit app
st.sidebar.title("Navegação")
page = st.sidebar.radio("Escolha uma página", ["Overview", "Proposições", "Despesas"])


if page == "Overview":
    overview_page()
elif page == "Proposições":
    proposicoes_page()
elif page == "Despesas":
    despesas_page()

