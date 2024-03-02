import paho.mqtt.publish as publish

publish.single('mqtt/test', 'Hello Everyone', hostname='test.mosquitto.org')
print('Message Published')
