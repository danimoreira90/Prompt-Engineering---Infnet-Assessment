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

def load_and_process_json(json_path):
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if isinstance(data, list) and isinstance(data[0], str):
            groups = re.split(r'\n\n(?=\*\*I\.)', data[0], flags=re.S)
            groups = [group.strip() for group in groups if group.strip()]
            return groups
        else:
            st.error("Estrutura inesperada: esperava-se uma string dentro da lista.")
            return None
    except FileNotFoundError:
        st.error("Arquivo JSON não encontrado.")
        return None
    except json.JSONDecodeError as e:
        st.error(f"Erro ao decodificar JSON: {e}")
        return None
    except Exception as e:
        st.error(f"Um erro inesperado ocorreu: {e}")
        return None

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

    try:
        with open(r"D:\Pastas\Infnet\Infnet - 2024.2\Engenharia de Prompts\AT\data\insights_distribuicao_deputados.json", 'r', encoding='iso-8859-1') as f:
            insights_despesas = json.load(f)
            st.write(insights_despesas) # Adicione aqui a exibição dos insights como desejar

        df_despesas = pd.read_parquet(r"D:\Pastas\Infnet\Infnet - 2024.2\Engenharia de Prompts\AT\data\serie_despesas_diárias_deputados.parquet")
        deputados = df_despesas['deputado_nome'].unique()
        deputado_selecionado = st.selectbox('Selecione um Deputado:', deputados)

        despesas_deputado = df_despesas[df_despesas['deputado_nome'] == deputado_selecionado]
        fig_despesas_tempo = px.bar(despesas_deputado, x='data_despesa', y='valor_despesa', title=f'Série Temporal de Despesas - {deputado_selecionado}')
        st.plotly_chart(fig_despesas_tempo)


    except FileNotFoundError:
        st.error("Arquivos de despesas não encontrados. Verifique o caminho.")
    except json.JSONDecodeError as e:
        st.error(f"Erro ao decodificar JSON: {e}")
    except Exception as e:
        st.error(f"Um erro ocorreu: {e}")  



# Proposições Page
def proposicoes_page():
    try:
        proposicoes = pd.read_parquet(r"D:\Pastas\Infnet\Infnet - 2024.2\Engenharia de Prompts\AT\data\proposicoes_deputados.parquet")
        st.title("Análise de Proposições")
        temas = ['Economia', 'Educação', 'Ciência']
        proposicoes_filtradas = proposicoes[proposicoes['Tema'].isin(temas)].head(10)
        for index, row in proposicoes_filtradas.iterrows():
            st.markdown(f"### {row['uri']}")
            st.markdown(f"**Tema:** {row['Tema']}")
            st.markdown(f"**Resumo:** {row['ementa']}")

        st.dataframe(proposicoes)

        json_path = r"D:\Pastas\Infnet\Infnet - 2024.2\Engenharia de Prompts\AT\data\sumarizacao_proposicoes.json"
        insights = load_and_process_json(json_path)
        if insights:
            st.subheader("Análise Detalhada das Proposições")
            for idx, insight in enumerate(insights, start=1):
                st.markdown(f"#### Análise {idx}")
                st.markdown(insight)
    except FileNotFoundError:
        st.error("Arquivos de proposições não encontrados. Verifique o caminho.")
    except Exception as e:
        st.error(f"Um erro ocorreu: {e}")



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

