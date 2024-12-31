import openai
import pandas as pd
import os
from keys import chave_openai

# Configure a chave da API da OpenAI
openai.api_key = chave_openai

# Função para gerar o briefing
def gerar_briefing_campanha(caminho_arquivo):
    try:
        # Carregar os dados da campanha
        campanha_df = pd.read_csv(caminho_arquivo)
        
        # Criar uma lista para armazenar os briefings
        briefings = []

        for _, campanha in campanha_df.iterrows():
            # Estruturar o comando para a API
            prompt = f"""
            Você é um especialista em marketing digital. Crie um briefing detalhado para um creator
            baseado nos seguintes dados de campanha:
            
            Nome da Campanha: {campanha.get('Nome da Campanha', 'Não informado')}
            Objetivo: {campanha.get('Objetivo', 'Não informado')}
            Público-Alvo: {campanha.get('Público-Alvo', 'Não informado')}
            Formato do Conteúdo Desejado: {campanha.get('Formato do Conteúdo Desejado', 'Não informado')}
            Canal de Divulgação: {campanha.get('Canal de Divulgação', 'Não informado')}
            Tipo de Conteúdo Postado: {campanha.get('Tipo de Conteúdo Postado', 'Não informado')}
            Ações e Comportamentos Esperados do Creator: {campanha.get('Ações e Comportamentos Esperados do Creator', 'Não informado')}
            Comportamentos Indesejados ou Proibidos: {campanha.get('Comportamentos Indesejados ou Proibidos', 'Não informado')}
            
            Inclua as seguintes informações no briefing:
            - Propósito da campanha
            - Público-alvo
            - Mensagens principais
            - Tom de voz
            - Diretrizes visuais e quaisquer detalhes relevantes.
            """

            # Solicitar à API o briefing
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=500,
                temperature=0.7
            )

            # Obter a resposta e armazenar
            briefing = response.choices[0].text.strip()
            briefings.append(briefing)

        # Adicionar a nova coluna ao DataFrame
        campanha_df['Briefing'] = briefings

        # Salvar o DataFrame atualizado no mesmo arquivo
        campanha_df.to_csv(caminho_arquivo, index=False, encoding='utf-8')

        return caminho_arquivo

    except Exception as e:
        return f"Erro ao gerar briefing: {e}"

# Usar a função com o caminho do arquivo gerado anteriormente
caminho_csv = "caminho_do_arquivo_previamente_salvo.csv"  # Substitua pelo caminho retornado do código anterior
resultado = gerar_briefing_campanha(caminho_csv)

# Exibir o resultado
if os.path.exists(resultado):
    print(f"Arquivo atualizado com sucesso: {resultado}")
else:
    print(resultado)
