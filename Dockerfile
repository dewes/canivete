from python:3.8

RUN pip install --upgrade

RUN mkdir /code
WORKDIR /code

EXPOSE 8000

COPY requirements.txt /code/
RUN pip install -r requirements.txt

RUN python -m spacy download pt

COPY ./canivete /code

CMD ["uvicorn", "canivete.main:app", "--host", "0.0.0.0", "--port", "8000"]
