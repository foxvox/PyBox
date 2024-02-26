from socket import *

port = 2500
maxSize = 1024
cs = socket(AF_INET, SOCK_DGRAM)

ipAddr = input('Server IP Address: ')
if ipAddr == '':
    ipAddr = 'localhost'
sa = (ipAddr, port)

while True:
    msg = input("<- ")
    cs.sendto(msg.encode(), sa)
    print("-> ", end='')
    sd, sa = cs.recvfrom(maxSize)  # maxSize: 최대 수신 바이트 수, cs: client data, ca: client address
    print(sd.decode())  #수신 데이터는 바이트 형 
