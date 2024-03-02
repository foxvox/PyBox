import paho.mqtt.subscribe as subscribe

def on_message(client, userdata, message):
    print("Topic: %s, Message: %s" % (message.topic, message.payload))

subscribe.callback(on_message, 'mqtt/multiple', hostname='test.mosquitto.org')
