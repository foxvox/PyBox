from socket import *

serverAddr = 'localhost'
serverPort = 2500
BUFFER = 1024
cs = socket(AF_INET, SOCK_DGRAM)
cs.connect((serverAddr, serverPort))        # 연결 논리적/가상적

for i in range(10):     # 10번 시도
    delay = 0.1     # seconds
    data = 'Hello message'

    while True:
        cs.send(data.encode())
        print('Waiting up to {} seconds for a reply'.format(delay))
        cs.settimeout(delay)
        try:
            data = cs.recv(BUFFER)
        except timeout:
            delay *= 2      # 대기시간 2배 증가
            if delay > 2.0:
                print("The server seems to be down")
                break
        else:
            print('Response: ', data.decode())
            break
