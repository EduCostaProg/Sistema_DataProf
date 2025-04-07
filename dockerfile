FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Copia o arquivo de dependências
COPY requirements.txt .

# Instala dependências do sistema necessárias para o mysqlclient
RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev

# Instala as dependências
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia o restante do código
COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


