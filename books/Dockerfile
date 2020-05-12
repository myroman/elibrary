FROM python:3.6

EXPOSE 5002

WORKDIR /books

COPY requirements.txt /books

RUN pip3 install -r requirements.txt

COPY api.py /books
COPY dbutils.py /books

CMD python3 api.py
