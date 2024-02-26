from socket import *

table = {'1': 'ont', '2': 'two', '3': 'three', '4': 'four', '5': 'five', \
         '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten'}

ss = socket()
addresss = ('', 2500)  # 빈문자열은 localhost랑 같다.
ss.bind(addresss)

ss.listen(1)
print('Waiting...')

c_s, c_a = ss.accept()
print('Connection from', c_a)

while True:
    data = c_s.recv(1024).decode()
    try:
        resp = table[data]  # key값을 넣어주면 value값을 return 해준다.
    except:
        c_s.send('Try again'.encode())
    else:
        c_s.send(resp.encode())

