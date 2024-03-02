import paho.mqtt.subscribe as subscribe

topics = 'mqtt/multiple'
msgCnt = 2

ml = subscribe.simple(topics, hostname='test.mosquitto.org',
                     retained=False, msg_count=msgCnt)
for i in range(msgCnt):
    print('Topic: ', ml[i].topic)
    print('Message: ', ml[i].payload.decode())
