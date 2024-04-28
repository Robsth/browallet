FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /wallet

COPY requirements.txt /wallet/
RUN pip install -r requirements.txt

COPY . /wallet/