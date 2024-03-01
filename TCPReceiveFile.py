from socket import *

cs = socket()
host = 'localhost'
port = 2500

cs.connect((host, port))  # connect to the server
cs.send("I am ready".encode())
fn = cs.recv(1024).decode()

with open('C:/DevPy/SP/new_' + fn, 'wb') as f:
    print('file opended') 
    print('receiving file...') 
    
    while True:
        data = cs.recv(8192)
        if not data:
            break    # if no more file exit
        f.write(data)  # write data to a file

print('C:/DevPy/SP/new_' + fn +' Download complete')
cs.close()
