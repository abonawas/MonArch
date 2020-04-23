FROM python:3.7-alpine
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
ARG BUST_CACHE=no
COPY . .
CMD ["python", "-u", "app.py"]

