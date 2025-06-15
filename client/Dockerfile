# Imagem base
FROM python:3.12-slim

# Diretório de trabalho no container
WORKDIR /app

# Copia os arquivos
COPY . .

# Instala dependências
RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

# Comando padrão
CMD ["bash"]
