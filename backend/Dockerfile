FROM python:3.11-slim

ENV PYTHONPATH=/app/backend \
    PORT=8000

WORKDIR /app

COPY server/requirements.txt /tmp/requirements.txt

RUN python -m pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt

COPY . /app/backend

WORKDIR /app

EXPOSE 8000

CMD ["python3","-m", "backend.server.server"]