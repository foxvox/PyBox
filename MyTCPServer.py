class TCPServer:
    def __init__(self, port):
        import socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('127.0.0.1', port))  #bind 함수 인자로 튜플을 넣어줘야함
        self.sock.listen(1)

    def Accept(self):
        self.c_sock, self.c_addr = self.sock.accept()
        return self.c_sock, self.c_addr

if __name__ == '__main__':  #다른 모듈에서 import해서 실행하면 실행이 안 됨.
    ss = TCPServer(2500)
    cs, ca = ss.Accept()
    print('수신메시지: ', cs.recv(1024).decode())
    msg = 'Hello Client'
    cs.send(msg.encode())
    cs.close()
