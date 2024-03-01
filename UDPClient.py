from socket import *
BUFSIZE = 1024
port = 2500

cs = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input("송신 메시지: ")
    cs.sendto(msg.encode(), ('localhost', port))
    sd, sa = cs.recvfrom(BUFSIZE)
    print('수신 메시지: ', sd.decode())


