# python 3.11
# Code taken from https://www.emqx.com/en/blog/how-to-use-mqtt-in-python

import random

import paho.mqtt.client as mqtt_client


broker = "137.142.164.255"
port = 1883
botID = -1 # Need to get botID from botID ros topic
topic = "python/mqtt"
# Generate a Client ID with the subscribe prefix.
client_id = f'subscribe-bot{botID}'
# username = 'Sauron'
# password = 'rOb0t1cs#'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION2,client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port, 60)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
