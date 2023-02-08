FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8501

COPY . .

ENTRYPOINT ["streamlit", "run", "temp_docker_app.py", "--server.port=8501", "--server.address=0.0.0.0"]