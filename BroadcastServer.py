from socket import *

ss = socket(AF_INET, SOCK_DGRAM)
ss.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
ss.bind(('', 10000))        # 인자 튜플 

while True:
    cd, ca = ss.recvfrom(1024)
    print(cd.decode()) 
    
