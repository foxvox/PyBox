from socket import *

port = int(input("Port No: "))
address = ("localhost", port)  #서버주소와 포트번호를 튜플형태로 할당
BUFSIZE = 1024

s = socket()
s.connect(address)  #상대방의 주소를 인자로 넘겨준다.

while True:
    msg = input("Message to send: ")
    s.send(msg.encode())  #msg에 저장된 문자열을 바이트로 변환 후 전송
    data = s.recv(BUFSIZE)  #바이트형태로 전송 받음
    print("Received message: %s" % data.decode()) 
    
    