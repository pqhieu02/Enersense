FROM python:3.11.4

WORKDIR /mqtt

COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev build-essential 

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["./start.sh"]