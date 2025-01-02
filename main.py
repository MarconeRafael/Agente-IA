import os
from simula_conect_publi import collect_campaign_details  # Importa a função do arquivo simula_conect_publi.py
from briefing import gerar_briefing_campanha            # Importa a função do arquivo briefing.py
from roteiro import gerar_roteiro_campanha              # Importa a função do arquivo roteiro.py
from embeddings import gerar_e_salvar_embeddings        # Importa a função do arquivo embeddings.py
import pandas as pd

def processar_briefing(campaign_df, caminho_arquivo):
    print("Gerando briefing da campanha...")
    try:
        briefing = gerar_briefing_campanha(caminho_arquivo)
        campaign_df['Briefing'] = briefing
    except Exception as e:
        print(f"Erro ao gerar briefing: {e}")
        return False
    return True

def processar_roteiro(campaign_df, caminho_arquivo):
    print("Gerando roteiro da campanha...")
    try:
        roteiro = gerar_roteiro_campanha(caminho_arquivo)
        campaign_df['Roteiro'] = roteiro
    except Exception as e:
        print(f"Erro ao gerar roteiro: {e}")
        return False
    return True

def main():
    # Coleta de detalhes
    print("Coletando detalhes da campanha...")
    caminho_arquivo = collect_campaign_details()
    if not os.path.exists(caminho_arquivo):
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return
    
    try:
        campaign_df = pd.read_csv(caminho_arquivo, encoding='utf-8')
        print("Detalhes da campanha carregados com sucesso.")
    except Exception as e:
        print(f"Erro ao carregar o arquivo CSV: {e}")
        return
    
    # Processamento
    if not processar_briefing(campaign_df, caminho_arquivo):
        return
    if not processar_roteiro(campaign_df, caminho_arquivo):
        return
    
    # Gerar embeddings
    caminho_embeddings = "csvs/embeddings.csv"

    # Verificar e criar o diretório se não existir
    diretorio = os.path.dirname(caminho_embeddings)
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
    
    print("Gerando e salvando embeddings...")
    caminho_atualizado = gerar_e_salvar_embeddings(caminho_embeddings)  # Passando o caminho correto para gerar e salvar os embeddings
    
    if caminho_atualizado:
        print(f"Embeddings gerados e salvos em: {caminho_atualizado}")
    else:
        print("Erro ao gerar embeddings.")

# Chamar a função main
if __name__ == "__main__":
    main()
