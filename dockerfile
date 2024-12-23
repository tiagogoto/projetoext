

FROM python:3.10.14-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .


CMD ["python", "src/app.py"]