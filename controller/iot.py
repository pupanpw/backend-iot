import requests
from config.config import ConfigMQTT


class IoTDetail:
    @staticmethod
    def mqttMsg(msg):
        print(msg)
        data = {
            'device': 'ESP-8266-Floor',
            'device_no': 'ESP8266/145',
            'status': 'some-status',
            'isActive': True,
            'event': msg,
            'created_by': 'mqtt'
        }
        print(ConfigMQTT.FLASK_URL+'/iot-pw')
        try:
            response = requests.post(
                ConfigMQTT.FLASK_URL + '/iot-pw', json=data)
            if response.status_code == 201:
                print('Event message sent to Flask application')
            else:
                print('Failed to send event message to Flask application')
        except requests.exceptions.RequestException as e:
            print('Error sending event message to Flask application:', str(e))
