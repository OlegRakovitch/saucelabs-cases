FROM python:3.5-alpine

WORKDIR /

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY ./client.py /client.py

CMD [ "python", "/client.py" ]
