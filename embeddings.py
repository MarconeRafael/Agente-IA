import os
import openai
import pandas as pd
from keys import chave_openai

# Configure a chave da API da OpenAI
openai.api_key = chave_openai

# Função para gerar embeddings e salvar no CSV
def gerar_e_salvar_embeddings(caminho_arquivo):
    try:
        # Verificar se o diretório do arquivo existe, se não, criar
        diretorio = os.path.dirname(caminho_arquivo)
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)  # Cria o diretório, se necessário

        # Verificar se o arquivo existe
        if not os.path.exists(caminho_arquivo):
            # Se o arquivo não existir, cria um CSV vazio com a coluna 'Embedding'
            df_vazio = pd.DataFrame(columns=['Embedding'])
            df_vazio.to_csv(caminho_arquivo, index=False, encoding='utf-8')

        campanha_df = pd.read_csv(caminho_arquivo)
        
        # Criar embeddings para cada linha do DataFrame
        embeddings = []  # Lista para armazenar os embeddings gerados

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
            try:
                response = openai.Embedding.create(
                    input=texto_para_embedding,
                    model="text-embedding-ada-002"
                )
                
                # Verificar se a resposta contém o embedding
                if 'data' in response and len(response['data']) > 0:
                    embedding = response['data'][0]['embedding']
                    embeddings.append(embedding)
                    print(f"Embedding gerado para a linha {index}.")  # Depuração
                else:
                    print(f"Nenhum embedding retornado para a linha {index}.")  # Depuração
                    embeddings.append("Erro ao gerar embedding")

            except openai.error.OpenAIError as e:
                print(f"Erro na API OpenAI para a linha {index}: {e}")
                embeddings.append("Erro ao gerar embedding")

        # Criar um novo DataFrame apenas com a coluna 'Embedding'
        if embeddings:
            embeddings_df = pd.DataFrame(embeddings, columns=['Embedding'])

            # Salvar o DataFrame com os embeddings
            embeddings_df.to_csv(caminho_arquivo, index=False, encoding='utf-8')
            print(f"Embeddings salvos com sucesso em {caminho_arquivo}.")
        else:
            print("Nenhum embedding foi gerado.")  # Depuração

        return caminho_arquivo

    except Exception as e:
        return f"Erro ao gerar e salvar embeddings: {e}"

# Exemplo de chamada da função
caminho_arquivo = "csvs/embeddings.csv"

# Chama a função para gerar e salvar os embeddings
resultado = gerar_e_salvar_embeddings(caminho_arquivo)

if "Erro" not in resultado:
    print(f"Embeddings gerados e salvos em: {resultado}")
else:
    print(resultado)
