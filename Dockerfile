# Usar a imagem oficial do Python
FROM python:3.10

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos do projeto para dentro do container
COPY . /app

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Definir variável de ambiente para o Token do GitHub
ENV GITHUB_TOKEN=""

# Executar o script principal
CMD ["python", "github_issue_creator.py"]
