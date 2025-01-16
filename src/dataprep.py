import os
import requests
import pandas as pd

# URL base da API
BASE_URL = 'https://dadosabertos.camara.leg.br/api/v2/'

OUTPUT_PATH = 'data/deputados.parquet'

def fetch_deputados():
    """
    Coleta informações dos deputados atuais da Câmara dos Deputados
    e salva os dados em formato Parquet.
    """
    url = BASE_URL + 'deputados'
    headers = {'Accept': 'application/json'}
    deputados = []
    pagina = 1

    try:
        while True:
            # Parâmetros para a API
            params = {'pagina': pagina, 'itens': 100}  
            print(f"Coletando página {pagina}...")
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()  

            data = response.json()
            deputados.extend(data.get('dados', []))

            # Verifica se há mais páginas
            if not data.get('links'):
                break
            proximo = next((link for link in data['links'] if link['rel'] == 'next'), None)
            if not proximo:
                break
            pagina += 1

        # Converte para DataFrame e salva em Parquet
        df = pd.DataFrame(deputados)
        os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
        df.to_parquet(OUTPUT_PATH, index=False)
        print(f"Dados salvos em {OUTPUT_PATH} com sucesso!")

    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
    except Exception as e:
        print(f"Erro no processamento: {e}")

if __name__ == "__main__":
    fetch_deputados()

def coleta_proposicoes(data_inicio, data_fim):
    temas = {
        'Economia': '40',
        'Educação': '46',
        'Ciência, Tecnologia e Inovação': '62'
    }
    dataframe_total = pd.DataFrame()

    for tema, codigo in temas.items():
        url = "https://dadosabertos.camara.leg.br/api/v2/proposicoes"
        params = {
            'dataInicio': data_inicio,
            'dataFim': data_fim,
            'codTema': [codigo],  # Tentando passar como uma lista
            'itens': 10
        }
        headers = {
            'Accept': 'application/json'
        }
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            dados = response.json().get('dados', [])
            if dados:
                dataframe_tema = pd.DataFrame(dados)
                dataframe_tema['Tema'] = tema
                dataframe_total = pd.concat([dataframe_total, dataframe_tema], ignore_index=True)
            else:
                print(f"Nenhum dado encontrado para o tema {tema}")
        else:
            print(f"Erro ao buscar dados para o tema {tema}: {response.status_code} - {response.text}")

    if not dataframe_total.empty:
        dataframe_total.to_parquet('data/proposicoes_deputados.parquet')
        print("Dados salvos com sucesso!")
    else:
        print("Nenhum dado foi coletado.")

# Chamada da função com as datas de início e fim desejadas
coleta_proposicoes('2024-01-01', '2024-12-31')