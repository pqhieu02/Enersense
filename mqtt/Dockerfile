FROM python:3.11.4-slim

WORKDIR /mqtt

COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    pkg-config \
    build-essential \
    default-libmysqlclient-dev

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["./start.sh"]