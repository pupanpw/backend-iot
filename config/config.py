import os
from os import environ
from dotenv import load_dotenv

load_dotenv()

DB_URL = environ.get('DB_URL')


class ConfigMQTT:
    MQTT_USERNAME = os.getenv('MQTT_USERNAME')
    FLASK_URL = os.getenv('FLASK_URL')
    MQTT_PASSWORD = os.getenv('MQTT_PASSWORD')
    MQTT_TOPIC = os.getenv('MQTT_TOPIC')
    MQTT_BROKER_IP = os.getenv('MQTT_BROKER_IP')
    MQTT_PORT = int(os.getenv('MQTT_PORT', 1883))
