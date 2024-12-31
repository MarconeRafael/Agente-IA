import os
from simula_conect_publi import collect_campaign_details  # Importa a função do arquivo simula_conect_publi.py
from briefing import gerar_briefing_campanha            # Importa a função do arquivo briefing.py
from roteiro import gerar_roteiro_campanha              # Importa a função do arquivo roteiro.py
from embeddings import gerar_e_salvar_embeddings       # Importa a função do arquivo embeddings.py
import pandas as pd

def main():
    # 1. Coletar detalhes da campanha e salvar em um CSV
    print("Coletando detalhes da campanha...")
    campaign_df = collect_campaign_details()  # Chama a função de coletar dados da campanha

    # Verifica se o retorno é um DataFrame, caso contrário, carrega um CSV
    if isinstance(campaign_df, pd.DataFrame):
        print("Detalhes da campanha coletados com sucesso.")
    else:
        print("Erro: A função collect_campaign_details não retornou um DataFrame.")
        return

    caminho_arquivo = "csvs/campanha.csv"  # Caminho para salvar o CSV
    campaign_df.to_csv(caminho_arquivo, index=False, encoding='utf-8')  # Salva os dados no CSV

    # 2. Gerar Briefing para a campanha
    print("Gerando briefing da campanha...")
    briefing = gerar_briefing_campanha(caminho_arquivo)  # Gera o briefing
    campaign_df['Briefing'] = briefing  # Adiciona o briefing ao DataFrame
    campaign_df.to_csv(caminho_arquivo, index=False, encoding='utf-8')  # Atualiza o CSV

    # 3. Gerar Roteiro para a campanha
    print("Gerando roteiro da campanha...")
    roteiro = gerar_roteiro_campanha(caminho_arquivo)  # Gera o roteiro
    campaign_df['Roteiro'] = roteiro  # Adiciona o roteiro ao DataFrame
    campaign_df.to_csv(caminho_arquivo, index=False, encoding='utf-8')  # Atualiza o CSV

    # 4. Gerar e salvar embeddings
    print("Gerando e salvando embeddings...")
    caminho_atualizado = gerar_e_salvar_embeddings(caminho_arquivo)  # Gera e salva os embeddings no CSV
    
    print(f"Processo concluído. O arquivo foi salvo em: {caminho_atualizado}")

if __name__ == "__main__":
    main()
