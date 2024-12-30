
import pandas as pd
def collect_campaign_details():
    print("Preencha as informações da campanha:\n")

    data = {
        "Nome da Campanha": input("Nome da Campanha (exemplo: 'Campanha Black Friday'): "),
        "Objetivo": input("Objetivo (exemplo: 'Aumentar vendas' ou 'Obter seguidores'): "),
        "Público-Alvo": input("Público-Alvo (exemplo: 'Jovens de 18-25 anos'): "),
        "Formato do Conteúdo Desejado": input("Formato do Conteúdo Desejado (exemplo: 'Reels, Stories, etc.'): "),
        "Canal de Divulgação": input("Canal de Divulgação (exemplo: 'Instagram, TikTok'): "),
        "Data de Início": input("Data de Início da Campanha (formato: DD/MM/AAAA): "),
        "Data de Término": input("Data de Término da Campanha (formato: DD/MM/AAAA): "),
        "Nicho de Mercado": input("Nicho de Mercado: "),
        "Tipo de Conteúdo Postado": input("Tipo de Conteúdo Postado (IGG ou UGC): "),
        "Produtos ou Serviços": input("Detalhes dos produtos ou serviços (incluindo envio e prazos): "),
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
    
    return campaign_df
teste = collect_campaign_details()
print(teste)