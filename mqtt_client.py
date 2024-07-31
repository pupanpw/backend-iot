import paho.mqtt.client as mqtt
from config.config import ConfigMQTT
from controller.iot import IoTDetail
config = ConfigMQTT()

client = mqtt.Client()
client.username_pw_set(config.MQTT_USERNAME, config.MQTT_PASSWORD)


def on_connect(client, userdata, flags, rc):
    print("Connected!", userdata, str(rc))

    client.subscribe(config.MQTT_TOPIC)


def on_message(client, userdata, msg):
    payload_str = str(msg.payload, 'utf-8')
    IoTDetail.mqttMsg(str(payload_str))


client.on_connect = on_connect
client.on_message = on_message


client.connect(config.MQTT_BROKER_IP, config.MQTT_PORT)

client.loop_forever()
client.disconnect()
