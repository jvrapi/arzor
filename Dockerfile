FROM python:3.12-slim

WORKDIR /app

# Instala ferramentas básicas e o 'build-essential'
# O build-essential é necessário para compilar as dependências de banco de dados (asyncpg, psycopg).
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl && rm -rf /var/lib/apt/lists/*

# Copia arquivos de configuração e código. 
# O 'pip install .' precisa do pyproject.toml para saber o que instalar.
COPY pyproject.toml .
COPY src ./src

# Instala o projeto e suas dependências usando pip.
# O '--no-cache-dir' é uma boa prática para manter o tamanho da imagem menor.
# O 'pip install .' lê o pyproject.toml e instala as dependências.
RUN pip install --no-cache-dir .

# Define a variável de ambiente PYTHONPATH para que o Python encontre o seu código.
ENV PYTHONPATH=/app/src

# NOVO: ENTRYPOINT define o executável principal. 
# ATUALIZADO: Voltando a usar o script 'arzor' definido em pyproject.toml.
# O 'arzor' executa a função 'main:run' que inicia o Uvicorn.
ENTRYPOINT ["arzor"]

