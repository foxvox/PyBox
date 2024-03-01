from socket import *

port = 2500
maxSize = 1024
ss = socket(AF_INET, SOCK_DGRAM)
ss.bind(('', port))  # 주소 결합, 인자는 튜플
print("Waiting for client...")

while True:
    print("<- ", end='')
    cd, ca = ss.recvfrom(maxSize)  # maxSize: 최대 수신 바이트 수, cs: client data, ca: client address
    print(cd.decode())  #수신 데이터는 바이트 형
    resp = input("-> ")
    ss.sendto(resp.encode(), ca)
