FROM python:3.6

EXPOSE 5002

WORKDIR /users

COPY requirements.txt /users

RUN pip3 install -r requirements.txt

COPY api.py /users
COPY dbutils.py /users

CMD python3 api.py
