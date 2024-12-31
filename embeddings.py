import openai
import pandas as pd
import os
from keys import chave_openai

# Configure a chave da API da OpenAI
openai.api_key = chave_openai

# Função para gerar embeddings e salvar no CSV
def gerar_e_salvar_embeddings(caminho_arquivo):
    try:
        # Carregar o CSV
        campanha_df = pd.read_csv(caminho_arquivo)
        
        # Verificar se a coluna 'Embedding' já existe
        if 'Embedding' not in campanha_df.columns:
            campanha_df['Embedding'] = ""

        # Criar embeddings para cada linha do DataFrame
        for index, row in campanha_df.iterrows():
            # Combine os campos relevantes da campanha em um único texto
            texto_para_embedding = f"""
            Nome da Campanha: {row.get('Nome da Campanha', 'Não informado')}
            Objetivo: {row.get('Objetivo', 'Não informado')}
            Público-Alvo: {row.get('Público-Alvo', 'Não informado')}
            Formato do Conteúdo Desejado: {row.get('Formato do Conteúdo Desejado', 'Não informado')}
            Canal de Divulgação: {row.get('Canal de Divulgação', 'Não informado')}
            Tipo de Conteúdo Postado: {row.get('Tipo de Conteúdo Postado', 'Não informado')}
            Ações e Comportamentos Esperados do Creator: {row.get('Ações e Comportamentos Esperados do Creator', 'Não informado')}
            Comportamentos Indesejados ou Proibidos: {row.get('Comportamentos Indesejados ou Proibidos', 'Não informado')}
            Briefing: {row.get('Briefing', 'Não informado')}
            Roteiro: {row.get('Roteiro', 'Não informado')}
            """
            
            # Gerar o embedding usando a API da OpenAI
            response = openai.Embedding.create(
                input=texto_para_embedding,
                model="text-embedding-ada-002"
            )
            
            # Salvar o embedding no DataFrame (armazenado como string para o CSV)
            embedding = response['data'][0]['embedding']
            campanha_df.at[index, 'Embedding'] = str(embedding)

        # Salvar o DataFrame atualizado no mesmo arquivo
        campanha_df.to_csv(caminho_arquivo, index=False, encoding='utf-8')

        return caminho_arquivo

    except Exception as e:
        return f"Erro ao gerar e salvar embeddings: {e}"

# Usar a função com o caminho do arquivo gerado anteriormente
caminho_csv = "caminho_do_arquivo_previamente_salvo.csv"  # Substitua pelo caminho correto
resultado = gerar_e_salvar_embeddings(caminho_csv)

# Exibir o resultado
if os.path.exists(resultado):
    print(f"Arquivo atualizado com embeddings: {resultado}")
else:
    print(resultado)
