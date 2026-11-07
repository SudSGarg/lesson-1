FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

ENV PORT=5555

ENV APP_ENV=Production

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 5555

CMD ["python", "app.py"]