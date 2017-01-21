# coding:utf-8
import socket

server_address = (HOST, PORT) = '', 888

address_family = socket.AF_INET
socket_type = socket.SOCK_STREAM
request_queue_size = 1

# Create a listening socket
listen_socket = listen_socket = socket.socket(
    address_family,
    socket_type
)
# Allow to reuse the same address
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind
listen_socket.bind(server_address)
# Activate
listen_socket.listen(request_queue_size)
# Get server host name and port
host, port = listen_socket.getsockname()[:2]
server_name = socket.getfqdn(host)
server_port = port
# Return headers set by Web framework/Web application
headers_set = []

tt = listen_socket.getsockname()
print tt[0]

a = ['haha', 'hihi', 'hoho']
print a[1]

b = ('haha', 'hihi', 'hoho')
print b[1]