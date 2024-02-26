from socket import *
import random

port = 2500
BUFFER = 1024
ss = socket(AF_INET, SOCK_DGRAM)
ss.bind(('localhost', port))
print('Listening...')

while True:
    data, addr = ss.recvfrom(BUFFER)

    if random.randint(1, 10) < 4:       # Packet is discarded. 30%만 응답
        print('Packet from {} lost!!!'.format(addr))
        continue

    print('Messgae is {!r} from {}'.format(data.decode(), addr))        # Display Message
    ss.sendto('ACK'.encode(), addr)     # ACK response
