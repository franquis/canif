import socket
import sys
import asyncio
from nats.aio.client import Client as NATS
from nats.aio.errors import ErrConnectionClosed, ErrTimeout, ErrNoServers

nc = NATS()

class DiscoveryProtocol(asyncio.DatagramProtocol):
    def __init__(self):
        super().__init__()
    def connection_made(self, transport):
        self.transport = transport
    def datagram_received(self, data, addr):
        nc.publish("can.message", data)

async def run(loop):
    await nc.connect("127.0.0.1:4222", loop=loop)

    # sid = await nc.subscribe("can.exec", "workers", help_request)
    t = loop.create_datagram_endpoint(DiscoveryProtocol,local_addr=('0.0.0.0',6000))
        

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
    # loop.run_forever()


"""
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('0.0.0.0', 6000)
print('Starting up on %s port %s' % server_address)
sock.bind(server_address)
print('Listening')
while True:
    
    data, address = sock.recvfrom(4096)
    print('received %s bytes from %s' % (len(data), address))
    # print(data)
    
    # if data:
    #     sent = sock.sendto(data, address)
    #     print('sent %s bytes back to %s' % (sent, address))
"""