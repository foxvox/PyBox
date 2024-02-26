from socket import *

# sa = ('192.168.0.255', 10000) => Broadcast Address
sa = ('<broadcast>', 10000)

# socket for broadcasting
cs = socket(AF_INET, SOCK_DGRAM)
cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while True:
    msg = input('Broadcast Message: ')
    cs.sendto(msg.encode(), sa)          # send broadcasting message
