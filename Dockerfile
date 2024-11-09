# Use a imagem base do Python
FROM python:3.12-slim

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie o arquivo de código para o container
COPY app.py .

# Instale as dependências necessárias (se houver)
# RUN pip install -r requirements.txt

# Defina o comando de execução da aplicação
CMD ["python", "app.py"]


