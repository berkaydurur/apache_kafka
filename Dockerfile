FROM python:3.10.0b1-buster

WORKDIR /.

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY producer.py .

CMD ["python","producer.py"]

FROM alpine

CMD consumer.sh