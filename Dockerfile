FROM python:3.9-slim
ENV PYTHONUNBUFFERED True
WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD exec gunicorn --bind :$PORT --workers 4 --threads 8 --timeout 0 app:app
