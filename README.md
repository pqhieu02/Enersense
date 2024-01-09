# Simple MQTT application

## Overview
The purpose of this project is to demonstrate a simple example of utilizing the MQTT technologies, python third parties library: FastAPI, paho-mqtt, etc.

## Component

This application comprises four core components: MQTT service, REST service, MySQL database and MQTT broker Mosquitto. 

#### MQTT service: 
- Take responsibility for creating a publisher to publish a message to the broker periodically, and a subscriber to listen and persist received messages. 
- The source code can be found in `/mqtt`
#### REST service: 
- A simple backend server managing migrations of the database, and exposing API to fetch the data in the MySQL database. 
- The source code can be found in `/backend`

#### MySQL server and Mosquitto
- MySQL is used by both of the services to store and persist data
- Mosquitto is a MQTT broker

## How to run locally
#### Backend
First and foremost, Go to the root directory of Backend:
```bash
cd backend
```

The commands to run the application locally vary based on the operating system:
- Windows:
    ```bash
    ./start.ps1
    ```

- Linux:
    ```bash
    ./start.sh
    ```

Alternatively, the application can be run using docker. Ensure that docker is installed and turned on, then run the following commands (Note: replace <image-name> with the image name you want):
```bash
docker build -t <image-name> .
docker run <image-name>
```

#### Mqtt
Go to the root directory of Mqtt:
```bash
cd mqtt
```

The commands to run the application locally vary based on the operating system:
- Windows:
    ```bash
    ./start.ps1
    ```

- Linux:
    ```bash
    ./start.sh
    ```

Alternatively, the application can be run using docker. Ensure that docker is installed and turned on, then run the following commands (Note: replace <image-name> with the image name you want):

```bash
docker build -t <image-name> .
docker run <image-name>
```

## How to run using docker
```bash
docker compose up -d
```

## Open MySQL terminal
```bash
docker compose exec mysql bash
```
The username and password for MySQL Server are both `root`

## Monitor log
```bash
docker compose up logs -f <service_name>
```
The options for service name are: `mqtt`, `backend`, `mysql`, `mosquitto`, which are for QTT service, REST service, MySQL server and the MQTT broker respectively

## Other information
- Swagger API documentation for REST server can be accessed `http://localhost:8000/docs`
- In Linux, if `start.sh` file does not have permission to be executed, try granting the script executable permission by running this command in the directory where the script is located: `chmod +x start.sh` 