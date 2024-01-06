import asyncio
import time
import uuid
import json
import paho.mqtt.client as mqtt
import logging

from service.charging_session_service import create_charging_session


class MqttClient:
    clients = []

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
        self._publishing_message = {}
        self.clients.append(self)

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
        message_info = self._client.publish(topic, payload=payload, qos=qos)
        self._publishing_message[message_info.mid] = message_info

    def disconnect(self):
        # When disconnecting, the library will not wait for
        # the unpublished messages. This is to avoid message lost 
        # when user attempt to shutdown gracefully
        for mid in self._publishing_message:
            message_info = self._publishing_message[mid]
            if not message_info.is_published():
                try:
                    message_info.wait_for_publish(2)
                    if not message_info.is_published(): raise Exception('timeout')
                except Exception as e:
                    self._logger.info(f'Failed to publish message, abort to disconnect. Reason: {e}')
        
        self._client.loop_stop()
        self._client.disconnect()
                    
    
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

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        loop.run_until_complete(create_charging_session(data))

        loop.close()
        create_charging_session(data)

    def _on_publish(self, client, userdata, mid):
        self._publishing_message.pop(mid, None)
        