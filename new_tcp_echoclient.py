from socket import *

#port = int(input("Port No: "))

address = ("localhost", 2500)  #서버주소와 포트번호를 튜플형태로 할당
BUF_SIZE = 1024

cs = socket()
cs.connect(address)  #상대방의 주소를 인자로 넘겨준다.

while True:
    msg = input("Message to send: ")
    try:
        n = cs.send(msg.encode())  #msg에 저장된 문자열을 바이트로 변환 후 전송
    except:
        print("송신 연결이 종료되있습니다")
        retry = input("계속? (y/n) ")

        if retry == 'n':
            cs.close() 
            break
        else:
            continue
    else:
        print("{} bytes sent".format(n))  #전송된 바이트 수

    try:
        data = cs.recv(BUF_SIZE)  #바이트형태로 전송 받음
        if not data:
            break 
    except:
        print("수신 연결이 종료되있습니다")
        cs.close()
        break
    else:
        print("Received message: %s" % data.decode())