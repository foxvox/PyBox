from socket import *

ECHO_PORT = 2500
BUF_SIZE = 1024

ss = socket()
ss.bind(('localhost', ECHO_PORT))  #튜플형태로 인자를 넘겨줌
ss.listen(1)
print("Waiting for clients...")
conn, (rh, rp) = ss.accept()
print("Connected by ", rh, rp)

while True:
    try:
        data = conn.recv(BUF_SIZE)
        if not data:            #Client가 정상 종료되면 data에 Null이 들어와서 참이 된다.
            print("정상 종료")
            break
    except:
        print("연결이 종료되었습니다")
        conn.close()
        break
    else:
        print(data.decode())

    try:
        conn.send(data)
    except:
        print("연결이 종료되었습니다")
        conn.close()
        break
