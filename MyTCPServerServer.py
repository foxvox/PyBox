import MyTcpServer as mts
import sys

port = 2500
if len(sys.argv) > 1:  #명령 실행시 포트를 지정하면 지정 포트 사용
    port = int(eval(sys.argv[1]))

ss = mts.TCPServer(port)
cs, ca = ss.Accept()  #socket과 address를 반환한다.
while True:
    print('Connected by ', ca[0], ca[1])  #address and port
    data = cs.recv(1024)
    if not data:
        break
    print('Received message: ', data.decode())
    cs.send(data)
cs.close()
