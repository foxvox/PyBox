# file_data = open('file.txt')
# print(file_data.readline(), end="")
# file_data.close()

# with open('file.txt') as file_data:
#     # 기본적으로 사용하는 함수를  with문 안에 사용하면 되며
#     # with문을 나올 때 close를 자동으로 불러줍니다.
#     print(file_data.readline(), end="")
    
from socket import *

port = 2500
ss = socket()
host = ''
ss.bind((host, port))
ss.listen(1)

print("Waiting for connection...")
cs, ca = ss.accept()  # establish connection with client
print('Connected from ', ca)

msg = cs.recv(1024)  # client will send welcome message when connected
print(msg.decode())

fileName = input('file name to send (C:/DevPy/SP/sample.bin): ')
print(f"Sending '{fileName}'")

fn = fileName.split('/')
cs.sendall(fn[-1].encode())  # send a file name without path

with open(fileName, 'rb') as f:
    cs.sendfile(f, 0)  # send file. use sendfile() or (f.read() and sendall())

    # data = f.read()
    # while data:
    #     cs.sendall(data)
    #     data = f.read()

print("Sending complete")
cs.close()
print("Connection closed") 



