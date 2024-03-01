from socket import *

port = 2500
BUFSIZE = 1024
ss = socket(AF_INET, SOCK_DGRAM)
ss.bind(('', port))  # 주소 결합, 인자는 튜플
print("수신 대기 중")

while True:
    cd, ca = ss.recvfrom(BUFSIZE)  # BUFSIZE: 최대 수신 바이트 수, cs: client data, ca: client address
    print("Received message: ", cd.decode())  #수신 데이터는 바이트 형
    print(ca)
    ss.sendto(cd, ca)
