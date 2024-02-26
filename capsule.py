def frame(start_ch, addr, seqNo, msg):
    addr = str(addr).zfill(2)
    seqNo = str(seqNo).zfill(4)
    length = str(len(msg)).zfill(4)
    temp =  chr(start_ch) + addr + seqNo + length + msg
    return temp

if __name__ == '__main__':
    start_ch = 0x05         # 시작문자
    addr = 2        # 주소
    seqNo = 1       # 순서번호

    msg = input('Your Message: ')
    capsule = frame(start_ch, addr, seqNo, msg)         # 프레임 구성
    print(capsule) 