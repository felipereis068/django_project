# Usar uma imagem oficial do Python como base
FROM python:3.11

# Instalar dependências para o mysqlclient
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential

# Definir o diretório de trabalho no container
WORKDIR /app

# Instalar o Django e as outras dependências
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Criar o ambiente virtual (venv)
RUN python -m venv /app/venv

# Ativar o ambiente virtual e garantir que seja ativado em sessões interativas
RUN echo "source /app/venv/bin/activate" >> ~/.bashrc

# Copiar o código do projeto para o container
COPY . .

# Expôr a porta 8000 para o Django
EXPOSE 8000

# Comando para rodar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
