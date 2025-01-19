# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import yaml
# import re
# import matplotlib.pyplot as plt
# from PIL import Image
# import json

# # Carregando os dados
# proposicoes = pd.read_parquet(r"D:\Pastas\Infnet\Infnet - 2024.2\Engenharia de Prompts\AT\data\proposicoes_deputados.parquet")
# despesas = pd.read_parquet(r"D:\Pastas\Infnet\Infnet - 2024.2\Engenharia de Prompts\AT\data\serie_despesas_diárias_deputados.parquet")
# caminho_json = r"D:\Pastas\Infnet\Infnet - 2024.2\Engenharia de Prompts\AT\data\insights_distribuicao_deputados.json"


# st.set_page_config(page_title="Análise de Dados da Câmara dos Deputados", layout="wide")

# # Aba Overview
# st.sidebar.title("Navegação")
# page = st.sidebar.radio("Selecione uma aba:", ('Overview', 'Despesas', 'Proposições'))

# if page == 'Overview':
#     st.title("Análise de Dados da Câmara dos Deputados")
#     st.markdown("""
#     Este projeto visa analisar dados da Câmara dos Deputados, fornecendo insights sobre as despesas parlamentares e as proposições legislativas.  
#     A Câmara dos Deputados é composta por 513 deputados, eleitos por representação proporcional para mandatos de quatro anos.  
#     Suas funções incluem legislar, representar o povo e fiscalizar o governo.

#     **Nesta aplicação, você encontrará:**

#     * **Despesas:** Visualizações de dados sobre os gastos dos deputados.
#     * **Proposições:** Resumos de proposições relevantes.

#     **Links Importantes:**

#     * [Câmara dos Deputados](https://www.camara.leg.br/)
#     """)


# # Aba Despesas
# elif page == 'Despesas':
#     st.title("Análise de Despesas Parlamentares")

#     # Pré-processamento (simplificado para exemplo) - Adaptar conforme necessário
#     despesas_agregadas = despesas.groupby('deputado_nome')['valor_despesa'].sum().reset_index()
#     despesas_agregadas = despesas_agregadas.sort_values('valor_despesa', ascending=False)


#     st.subheader("Top 10 Deputados com Maiores Despesas")
#     fig_despesas = px.bar(despesas_agregadas.head(10), x='deputado_nome', y='valor_despesa', title='Top 10 Deputados com Maiores Despesas')
#     st.plotly_chart(fig_despesas)

#     st.subheader("Distribuição das Despesas")
#     fig_dist = px.histogram(despesas, x='valor_despesa', title='Distribuição das Despesas')
#     st.plotly_chart(fig_dist)


# # Aba Proposições
# elif page == 'Proposições':
#     st.title("Análise de Proposições")

#     # Pré-processamento (simplificado para exemplo) - Adaptar conforme necessário
#     temas = ['Economia', 'Educação', 'Ciência']
#     proposicoes_filtradas = proposicoes[proposicoes['Tema'].isin(temas)].head(10)

#     for index, row in proposicoes_filtradas.iterrows():
#         st.subheader(row['uri'])
#         st.markdown(f"**Tema:** {row['Tema']}")
#         st.markdown(f"**Resumo:** {row['ementa']}") # Substituir por um resumo mais elaborado se necessário.
#         st.markdown("---")

# def fix_encoding(text):
#     text = text.replace('Ã¢', 'â')
#     text = text.replace('Ã£', 'ã')
#     text = text.replace('Ã³', 'ó')
#     text = text.replace('Ã§', 'ç')
#     text = text.replace('Ã¼', 'ü')
#     text = re.sub(r'Ã\w+', lambda m: m.group(0).replace('Ã', ''), text) #catch other possibilities

#     return text


# try:
#     with open('./data/config.yaml', 'r', encoding='utf-8') as file:
#         config = yaml.safe_load(file)
#         overview_summary = config['overview_summary']
#         overview_summary = fix_encoding(overview_summary)

# except FileNotFoundError:
#     overview_summary = "Arquivo config.yaml não encontrado."
# except KeyError:
#     overview_summary = "Chave 'overview_summary' não encontrada no arquivo config.yaml."
# except yaml.YAMLError as e:
#     overview_summary = f"Erro ao ler o arquivo YAML: {e}"


# st.title('Dashboard - Câmara dos Deputados (ago/2024)')
# st.markdown(overview_summary)

# def overview_page():
#     st.title("Overview")

#     # Texto resumido (assumindo que este código já existe de response2)
#     st.write("Aqui vai um texto resumido sobre os dados da Câmara dos Deputados.  Este texto descreve brevemente o conteúdo dos datasets utilizados, destacando as informações chave disponíveis para análise.")


#     # Carregando e exibindo a imagem
#     try:
#         img = Image.open(r"D:\Pastas\Infnet\Infnet - 2024.2\Engenharia de Prompts\AT\data\distribuicao_deputados.png")
#         st.markdown("<h3 style='text-align: center;'>Distribuição dos Deputados</h3>", unsafe_allow_html=True)
#         st.image(img, use_container_width=True)
#     except FileNotFoundError:
#         st.error("Imagem 'distribuicao_deputados.png' não encontrada. Certifique-se de que o caminho está correto.")


# def proposicoes_page():
#     st.title("Proposições")
#     # Código para análise e visualização das proposições (de response1 ou response2)
#     st.write("Análise de proposições")


# def despesas_page():
#     st.title("Despesas")
#     # Código para análise e visualização das despesas (de response1 ou response2)
#     st.write("Aqui seria a análise de despesas")

# def carregar_insights(caminho_json):
#     try:
#         with open(caminho_json, 'r') as f:
#             dados = json.load(f)
#             return dados['insights']
#     except FileNotFoundError:
#         st.error(f"Arquivo JSON não encontrado em: {caminho_json}")
#         return None
#     except KeyError:
#         st.error(f"Chave 'insights' não encontrada no arquivo JSON: {caminho_json}")
#         return None


# # Streamlit app
# st.sidebar.title("Navegação")
# page = st.sidebar.radio("Escolha uma página", ["Overview", "Proposições", "Despesas"])


# if page == "Overview":
#     overview_page()
# elif page == "Proposições":
#     proposicoes_page()
# elif page == "Despesas":
#     despesas_page()


import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import json
import yaml
import re

# Configuração da página
st.set_page_config(page_title="Análise de Dados da Câmara dos Deputados", layout="wide")

# Carregamento de dados
def load_data():
    proposicoes = pd.read_parquet(r"./data/proposicoes_deputados.parquet")
    despesas = pd.read_parquet(r"./data/serie_despesas_diárias_deputados.parquet")
    return proposicoes, despesas

proposicoes, despesas = load_data()

# Sidebar para navegação
st.sidebar.title("Navegação")
page = st.sidebar.radio("Selecione uma aba:", ('Overview', 'Despesas', 'Proposições', 'Insights'))

# Função para corrigir encoding
def fix_encoding(text):
    corrections = {
        'Ã¢': 'â', 'Ã£': 'ã', 'Ã³': 'ó', 'Ã§': 'ç', 'Ã¼': 'ü',
        'Ã': 'A', 'Ã©': 'é', 'Ãª': 'ê', 'Ã­': 'í'
    }
    for wrong, correct in corrections.items():
        text = text.replace(wrong, correct)
    return text

# Carrega e processa o arquivo de configuração YAML
def load_overview_summary():
    try:
        with open('./data/config.yaml', 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
            overview_summary = config['overview_summary']
            return fix_encoding(overview_summary)
    except FileNotFoundError:
        return "Arquivo config.yaml não encontrado."
    except KeyError:
        return "Chave 'overview_summary' não encontrada no arquivo config.yaml."
    except yaml.YAMLError as e:
        return f"Erro ao ler o arquivo YAML: {e}"

# Overview Page
def overview_page():
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



    st.title("Overview da Câmara dos Deputados")
    

    st.markdown(load_overview_summary())
    try:
        st.title('Dashboard - Câmara dos Deputados (ago/2024)')
        img = Image.open(r"./data/distribuicao_deputados.png")
        st.image(img, caption="Distribuição dos Deputados", use_container_width=True)
    except FileNotFoundError:
        st.error("Imagem 'distribuicao_deputados.png' não encontrada.")

# Despesas Page
def despesas_page():
    st.title("Análise de Despesas Parlamentares")

    # Agregando dados de despesas
    despesas_agregadas = despesas.groupby('deputado_nome')['valor_despesa'].sum().reset_index().sort_values('valor_despesa', ascending=False)

    # Gráfico de barras para os Top 10 Deputados com Maiores Despesas
    fig_despesas = px.bar(
        despesas_agregadas.head(10),
        x='deputado_nome',
        y='valor_despesa',
        title='Top 10 Deputados com Maiores Despesas',
        labels={'deputado_nome': 'Nome do Deputado', 'valor_despesa': 'Valor Total das Despesas (R$)'},
        color='valor_despesa',
        color_continuous_scale=px.colors.sequential.Viridis
    )
    fig_despesas.update_layout(
        xaxis_title='Nome do Deputado',
        yaxis_title='Total de Despesas (R$)',
        xaxis={'categoryorder': 'total descending'}
    )
    st.plotly_chart(fig_despesas)

    # Histograma para a Distribuição das Despesas
    fig_dist = px.histogram(
        despesas,
        x='valor_despesa',
        nbins=50,
        title='Distribuição das Despesas',
        labels={'valor_despesa': 'Valor da Despesa (R$)'}
    )
    fig_dist.update_layout(
        xaxis_title='Valor da Despesa (R$)',
        yaxis_title='Frequência',
        bargap=0.2
    )
    st.plotly_chart(fig_dist)

    st.markdown("""
    **Observações:**
    - O gráfico de barras acima mostra os dez deputados com as maiores despesas totais.
    - O histograma detalha a distribuição de todas as despesas registradas, ajudando a identificar padrões de gastos.
    """)


# Proposições Page
def proposicoes_page():
    st.title("Análise de Proposições")
    temas = ['Economia', 'Educação', 'Ciência']
    proposicoes_filtradas = proposicoes[proposicoes['Tema'].isin(temas)].head(10)
    for index, row in proposicoes_filtradas.iterrows():
        st.markdown(f"### {row['uri']}")
        st.markdown(f"**Tema:** {row['Tema']}")
        st.markdown(f"**Resumo:** {row['ementa']}")


def load_insights():
    try:
        with open(r"D:\Pastas\Infnet\Infnet - 2024.2\Engenharia de Prompts\AT\data\insights_distribuicao_deputados.json", 'r', encoding='iso-8859-1') as f:
            insights_data = json.load(f)
            insights_content = insights_data['insights']

        insights_cleaned = re.sub(r"^##.*?\n\n", "", insights_content, flags=re.S)

        insights_list = re.split(r"\n\*\*(\d+)\.\s*", insights_cleaned)[1:]
        
        st.subheader("Insights sobre a Distribuição de Deputados")

        for i in range(0, len(insights_list), 2):
            insight_number = insights_list[i]
            insight_text = insights_list[i+1].strip()
            st.markdown(f"Insight {insight_number}: {insight_text}")
            st.markdown("---")

    except FileNotFoundError:
        st.error("Arquivo não encontrado. Verifique o caminho especificado.")
    except KeyError:
        st.error("Chave 'insights' não encontrada no arquivo JSON.")
    except json.JSONDecodeError as e:
        st.error(f"Erro ao decodificar JSON: {e}")
    except Exception as e:
        st.error(f"Um erro ocorreu: {e}")

# Renderizando as páginas
if page == 'Overview':
    overview_page()
elif page == 'Despesas':
    despesas_page()
elif page == 'Proposições':
    proposicoes_page()
elif page == 'Insights':
    load_insights()

