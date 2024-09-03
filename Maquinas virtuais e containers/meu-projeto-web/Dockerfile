# Use a imagem oficial do Python como base
FROM python:3.9-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos do projeto para o contêiner
COPY . /app

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Defina a variável de ambiente para o Flask
ENV FLASK_APP=app.py

# Exponha a porta que o Flask usará
EXPOSE 5000

# Execute o aplicativo Flask
CMD ["flask", "run", "--host=0.0.0.0"]
