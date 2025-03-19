FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY mqtt2influx.py .

CMD ["python", "mqtt2influx.py"]
