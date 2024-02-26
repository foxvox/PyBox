from socket import *

cs = create_connection(('localhost', 2500))

msg = "Client Message"
print('sending {}'.format(msg))

cs.sendall(msg.encode())

data = cs.recv(1024)
print('received {}'.format(data.decode()))
print('closing socket')
cs.close()
