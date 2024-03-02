import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("test.mosquitto.org", 1833, 60)
rc, mid = client.publish("mqtt/test", "Hello YunEunSeo")
print(str(rc))
