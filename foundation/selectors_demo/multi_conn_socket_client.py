import socket

messages = [b'This is the message. ',
            b'It will be sent ',
            b'in parts.',
            ]
server_address = ('127.0.0.1', 8080)

socks = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for i in range(5)]
print(socks)
print('connecting to %s port %s' % server_address)
for s in socks:
    s.connect(server_address)

for message in messages:
    for s in socks:
        print('%s: sending "%s"' % (s.getsockname(), message))
        s.send(message)

    for s in socks:
        data = s.recv(1024)
        print('%s: received "%s"' % (s.getsockname(), data))
        if not data:
            print('closing socket', s.getsockname())
