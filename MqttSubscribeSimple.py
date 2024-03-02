import paho.mqtt.subscribe as subscribe

topics = 'mqtt/test'
m = subscribe.simple(topics, hostname='test.mosquitto.org',
                     retained=False, msg_count=1)
print(m.topic)
print(m.payload.decode())