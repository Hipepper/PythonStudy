import socket

sock = socket.socket()
sock.bind(("127.0.0.1", 8080))
sock.listen(5)
conn, addr = sock.accept()
content = conn.recv(1024)
print(content.decode())
conn.send(b'jieshouwanbi')
conn.close()
sock.close()
