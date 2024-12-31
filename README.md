# Projeto: Sistema de Gerenciamento de Campanhas para Influenciadores

Este projeto visa criar um sistema que gerencia campanhas de marketing para influenciadores digitais. O sistema coleta dados sobre campanhas, gera briefings detalhados, sugere roteiros e utiliza embeddings para armazenar e reutilizar informações de futuras interações com base nos dados de campanhas anteriores.

## Requisitos

Para rodar este projeto, você precisa de:

- Python 3.7 ou superior
- Bibliotecas Python:
  - `openai`
  - `pandas`
- Uma chave de API da OpenAI (para gerar briefings e roteiros através da API)
- Arquivo CSV para armazenar dados da campanha

## Instalação

1. **Clone o repositório ou baixe os arquivos do projeto.**

   ```bash
   git clone https://github.com/seu-usuario/projeto-campanha-influenciadores.git
   cd projeto-campanha-influenciadores
# Projeto: Sistema de Gerenciamento de Campanhas para Influenciadores

Este projeto visa criar um sistema que gerencia campanhas de marketing para influenciadores digitais. O sistema coleta dados sobre campanhas, gera briefings detalhados, sugere roteiros e utiliza embeddings para armazenar e reutilizar informações de futuras interações com base nos dados de campanhas anteriores.

## Requisitos

Para rodar este projeto, você precisa de:

- Python 3.7 ou superior
- Bibliotecas Python:
  - `openai`
  - `pandas`
- Uma chave de API da OpenAI (para gerar briefings e roteiros através da API)
- Arquivo CSV para armazenar dados da campanha

## Instalação

1. **Clone o repositório ou baixe os arquivos do projeto.**

   ```bash
   git clone https://github.com/seu-usuario/projeto-campanha-influenciadores.git
   cd projeto-campanha-influenciadores
2. **Crie e ative um ambiente virtual (opcional, mas recomendado).**
    python -m venv venv
    source venv/bin/activate  # No Linux/Mac
    venv\Scripts\activate     # No Windows
3. **Instale as dependências necessárias.**
    pip install -r requirements.txt
3.1 *Ou, se preferir instalar manualmente:*
    pip install openai pandas
4. **Vá para o site da OpenAI e gere uma chave de API.**
    Crie um arquivo chamado keys.py no seu diretório e adicione a chave da API da OpenAI:
    chave_openai = 'sua_chave_aqui'


Estrutura do Projeto

O projeto é dividido em diferentes scripts, cada um responsável por uma parte do processo:

    simula_conect_publi.py: Coleta os detalhes da campanha, como nome, objetivo, público-alvo, etc.
    briefing.py: Gera um briefing detalhado para a campanha com base nos dados coletados, utilizando a API da OpenAI.
    roteiro.py: Sugere um roteiro criativo para o influenciador, também com a ajuda da API da OpenAI.
    embeddings.py: Utiliza embeddings para armazenar e reutilizar informações de futuras interações com base nos dados de campanhas anteriores.
    main.py: Chama todos os scripts acima, em sequência, para executar o fluxo completo do sistema.

Como Rodar o Projeto

    Garanta que você tenha o ambiente virtual ativado (se estiver utilizando).

    Execute o script principal (main.py). Este script chama todos os outros scripts em sequência:
    python main.py
O fluxo do programa será:

    Primeiro, coletará os detalhes da campanha.
    Em seguida, gerará o briefing da campanha.
    Depois, sugerirá um roteiro para o influenciador.
    Por fim, armazenará as informações usando embeddings para reutilização futura.

Verifique o arquivo CSV gerado. Após a execução, o arquivo CSV será atualizado com as informações coletadas e o briefing gerado. O arquivo será salvo no mesmo diretório onde o script foi executado.