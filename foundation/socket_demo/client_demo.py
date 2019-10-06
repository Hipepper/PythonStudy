import socket

sock = socket.socket()
sock.connect(("127.0.0.1", 8080))
sock.send(b"hello")
content = sock.recv(1024)
print(content.decode())
sock.close()
