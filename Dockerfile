FROM python:3.10-slim-buster

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 libegl1-mesa-dev  -y

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY /src .

CMD ["python", "main.py"]