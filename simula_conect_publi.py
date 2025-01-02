import pandas as pd
import os

def collect_campaign_details():
    print("Preencha as informações da campanha:\n")

    data = {
        "Nome da Campanha": input("Nome da Campanha (exemplo: 'Campanha Black Friday'): "),
        "Objetivo": input("Objetivo (exemplo: 'Aumentar vendas' ou 'Obter seguidores'): "),
        "Público-Alvo": input("Público-Alvo (exemplo: 'Jovens de 18-25 anos'): "),
        "Formato do Conteúdo Desejado": input("Formato do Conteúdo Desejado (exemplo: 'Reels, Stories, etc.'): "),
        "Canal de Divulgação": input("Canal de Divulgação (exemplo: 'Instagram, TikTok'): "),
        "Nicho de Mercado": input("Nicho de Mercado: "),
        "Ações e Comportamentos Esperados do Creator": input(
            "Ações e Comportamentos Esperados do Creator (exemplo: 'Interagir com seguidores, criar conteúdos engajadores'): "
        ),
        "Comportamentos Indesejados ou Proibidos": input(
            "Comportamentos Indesejados ou Proibidos (exemplo: 'Falar mal da marca, utilizar linguagem ofensiva'): "
        ),
        "Informações Adicionais": input("Informações Adicionais: ")
    }
    
    # Criação do DataFrame
    campaign_df = pd.DataFrame([data])
    
    # Definir o nome e o caminho do arquivo CSV
    file_name = "csvs/campanha_detalhes.csv"
    file_path = os.path.join(os.getcwd(), file_name)
    
    # Salvar o DataFrame em CSV
    campaign_df.to_csv(file_path, index=False, encoding='utf-8')
    
    print(f"Detalhes da campanha salvos em: {file_path}")
    
    # Retornar o caminho do arquivo
    return file_path

# Chamando a função
#caminho_csv = collect_campaign_details()
#print(f"Arquivo salvo no caminho: {caminho_csv}")
