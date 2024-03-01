from socket import *

port = 2500
BUFSIZE = 1024

ss = socket()
ss.bind(('localhost', port))  #튜플형태로 인자를 넘겨줌
ss.listen(1)        # 최대 대기 클리이언트 수

cs, (remote_host, remote_port) = ss.accept()  #연결소켓과 연결주소(IP주소, 포트번호)반환 / 튜플언팩킹방식으로 할당받음

while True:
    data = cs.recv(BUFSIZE)

    if not data:
        break

    print("Received message: ", data.decode())  #수신된 데이터는 바이트 형이기 때문에 decode()해서 문자열로 변환
    cs.send(data) 

cs.close()
