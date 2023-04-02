FROM python:3.11-slim

WORKDIR /app

COPY src/ ./src
COPY requirements.txt ./
COPY run.py ./

RUN pip3 install -r requirements.txt

CMD python3 run.py