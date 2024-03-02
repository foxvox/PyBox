import paho.mqtt.client as mqtt

topic = "mqtt/test"

# rc means response code
def OnConnect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic)

def OnMessage(client, userdata, msg):
    print(msg.topic + " " + msg.payload.decode())
    print("Topic: ", msg.topic, "Message: ", str(msg.payload))

client = mqtt.Client()
client.on_connect = OnConnect
client.on_message = OnMessage

client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()