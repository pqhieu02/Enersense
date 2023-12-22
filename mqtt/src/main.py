
import os
import logging
import random
import time
from dotenv import load_dotenv
from lib.mqtt_client import MqttClient
from lib.helper import get_default_logging_handler


load_dotenv()
BROKER_ADDRESS = os.getenv('BROKER_ADDRESS')
TOPIC = 'charger/1/connector/1/session/1'

logger = logging.getLogger('root')
logger.setLevel(logging.INFO)
logger.addHandler(get_default_logging_handler())

logger.info('MQTT app version 1.0')

def main():
    # Publisher
    publisher = MqttClient(BROKER_ADDRESS)
    publisher.connect_and_wait()

    # Subscriber
    subscriber = MqttClient(BROKER_ADDRESS)
    subscriber.connect_and_wait()

    if (not publisher.is_connected() or not subscriber.is_connected()):
        logger.error('Failed to create MQTT connections. Abort')

    subscriber.subscribe(TOPIC, 1)

    while True:
        payload = str({
            'session_id': 1, 
            'energy_delivered_in_kWh': random.randint(1, 100),
            'duration_in_seconds':random.randint(1, 100), 
            'session_cost_in_cents': random.randint(1, 100)
        })
        publisher.publish(TOPIC, 1, payload=payload)
        time.sleep(3)

if __name__ == '__main__':
    main()
