from socket import *

port = int(2500)
address = ('127.0.0.1', port)  #서버주소와 포트번호를 튜플형태로 할당
BUFSIZE = 1024

s = socket(AF_INET, SOCK_STREAM) 
s.connect(address)  #상대방의 주소를 인자로 넘겨준다. 

while True:
    msg = input("Message to send: ")
    s.send(msg.encode())  #msg에 저장된 문자열을 바이트로 변환 후 전송
    rMsg = s.recv(BUFSIZE)  #바이트형태로 전송 받음
    if not rMsg:
        break
    print("Received message: %s" % rMsg.decode()) 
    
    