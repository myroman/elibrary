FROM python:3.6

EXPOSE 5000

WORKDIR /elibrary

COPY requirements.txt /elibrary

RUN pip3 install -r requirements.txt

COPY api.py /elibrary
COPY dbutils.py /elibrary

CMD python3 api.py
