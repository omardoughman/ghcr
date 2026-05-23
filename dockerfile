FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN mkdir -p build

CMD ["python", "main.py"]
