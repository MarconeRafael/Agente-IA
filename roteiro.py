import openai
import pandas as pd
import os
from keys import chave_openai

# Configure a chave da API da OpenAI
openai.api_key = chave_openai

def criar_prompt_roteiro(campanha):
    return f"""
    Você é um especialista em criação de conteúdo digital. Crie uma sugestão de roteiro para um creator
    baseado nos seguintes dados de campanha:
    
    Nome da Campanha: {campanha.get('Nome da Campanha', 'Não informado')}
    Objetivo: {campanha.get('Objetivo', 'Não informado')}
    Público-Alvo: {campanha.get('Público-Alvo', 'Não informado')}
    Formato do Conteúdo Desejado: {campanha.get('Formato do Conteúdo Desejado', 'Não informado')}
    Canal de Divulgação: {campanha.get('Canal de Divulgação', 'Não informado')}
    Tipo de Conteúdo Postado: {campanha.get('Tipo de Conteúdo Postado', 'Não informado')}
    Ações e Comportamentos Esperados do Creator: {campanha.get('Ações e Comportamentos Esperados do Creator', 'Não informado')}
    Comportamentos Indesejados ou Proibidos: {campanha.get('Comportamentos Indesejados ou Proibidos', 'Não informado')}
    
    Sugira uma sequência de ideias, tópicos ou cenas que o creator pode explorar no vídeo.
    Caso não seja possível sugerir, deixe em branco.
    """

def gerar_roteiro_campanha(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        return f"Arquivo não encontrado: {caminho_arquivo}"
    
    try:
        campanha_df = pd.read_csv(caminho_arquivo)
        roteiros = []

        for _, campanha in campanha_df.iterrows():
            prompt = criar_prompt_roteiro(campanha)
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um assistente de criação de conteúdo digital."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.7
            )
            roteiro = response['choices'][0]['message']['content'].strip() or "Não foi possível gerar um roteiro."
            roteiros.append(roteiro)

        campanha_df['Roteiro'] = roteiros
        novo_caminho = caminho_arquivo.replace(".csv", "_com_roteiro.csv")
        campanha_df.to_csv(novo_caminho, index=False, encoding='utf-8')
        return novo_caminho

    except openai.error.OpenAIError as e:
        return f"Erro na API OpenAI: {e}"
    except Exception as e:
        return f"Erro ao gerar roteiro: {e}"
