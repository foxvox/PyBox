import asyncio
class EchoServerProtocol():
    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        msg = data.decode()
        print('Received %r from %s' % (msg, addr))
        print('Send %r to %s' % (msg, addr))
        self.transport.sendto(data, addr)

async def main():
    print("Stating UDP server")

    # 현재의 이벤트 루프를 가져온다.
    loop = asyncio.get_running_loop()

    # (transport, protocol) 객체가 반환된다. transport는 연결객체이고,
    # protocol은 연결에서 발생하는 이벤트를 위한 cassback이 정의된 클래스 객체이다.
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: EchoServerProtocol(), ('127.0.0.1', 2500))
    # print(type(protocol))

    try:
        await asyncio.sleep(3600)   # Server for 1 hour.
    finally:
        transport.close()

asyncio.run(main())

