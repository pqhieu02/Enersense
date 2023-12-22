import time
import uuid
import json
import paho.mqtt.client as mqtt
import logging

from service.charging_session_service import create_charging_session


class MqttClient:
    def __init__(self,
                 broker_address: str,
                 port: int = 1883,
                 ):
        self._id = str(uuid.uuid4())
        self._client = mqtt.Client(self._id)
        self._client.on_connect = self._on_connect
        self._client.on_message = self._on_message

        self._broker_address = broker_address
        self._port = port
        self._subscribed_topics = []

        self._logger = logging.getLogger(f'MqttClient-{self._id}')

    def connect_and_wait(self, timeout_second: int = 5):
        try:
            self._client.connect(self._broker_address, self._port)
            self._client.loop_start()

            start_time = time.time()
            while (not self._client.is_connected()):
                time.sleep(1)
                now = time.time()
                if now - start_time > timeout_second:
                    raise Exception('Broker does not acknowledge client CONNECT message')
        except Exception as e:
            self._logger.error(
                f'Failed to connect to {self._broker_address}:{self._port}. Reason: {e}'
            )

    def subscribe(self, topic: str, qos: int = 0):
        return self._client.subscribe(topic, qos)

    def publish(self, topic, qos, payload):
        return self._client.publish(topic, payload=payload, qos=qos)

    def is_connected(self):
        return self._client.is_connected()

    def _on_connect(self, client, userdata, flags, rc):
        self._logger.info(
            f'Successfully connect to {self._broker_address}:{self._port}'
        )

    def _on_message(self, client, userdata, msg):
        payload = msg.payload.decode()
        self._logger.info(
            f'Message on topic {msg.topic}: {payload}'
        )
        data = json.loads(payload.replace("'", '"'))
        create_charging_session(data)

        