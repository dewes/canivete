from python:3.8

RUN pip install --upgrade

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

CMD uvicorn main:app --reload