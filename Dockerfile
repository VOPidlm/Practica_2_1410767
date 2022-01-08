FROM python:3.8.2-slim-buster

COPY . /app
WORKDIR /app

RUN mkdir ./files

RUN pip install -r Requirements.txt

CMD [ "python", "./Practica_2_Inventario_1410767.py"]
