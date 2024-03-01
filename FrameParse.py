# what's parcing?
# 어떤 문장을 분석하거나 문법적 관계를 해석하는 행위
# 프로그램을 compile하는 과정에서 특정 프로그래밍 언어가 제시하는
# 문법을 잘 지켜서 작성하였는지 compiler가 검사하는 것

from socket import *
import capsule
size = 5        # 페이로드 size
cs = socket()
cs.connect(('localhost', 2500))

head = 0x05
addr = 1
seqNo = 1
frame_seq = ''
msg = "Hello World"
print("전송메시지: ", msg)

# 메시지 단편화
for i in range(0, len(msg), size):
    frame_seq += capsule.frame(head, addr, seqNo, msg[i: i + size])
    seqNo += 1      # 순서번호 증가

cs.send(frame_seq.encode())         # 프레임 전송
msg = cs.recv(1024).decode()        # 프레임 수신 
print("수신프레임: ", msg)
r_frame = msg.split(chr(0x05))      # 프레임 분할
del r_frame[0]      # 첫번째 프레임요소는 빈문자열이므로 제거
p_msg = ''

for field in r_frame:
    # index 0~9까지 10개에는 페이로드 이외에 헤더가 들어있다.
    # p_msg += field[10: (10 + int(field[6: 10]))]        # field[6: 10] 6~9 4바이트에 페이로드 size가 문자열로 들어있다. 
    p_msg += field[10:]

print("복원메시지: ", p_msg)
cs.close() 
