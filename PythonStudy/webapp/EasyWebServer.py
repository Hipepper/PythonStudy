#!/usr/bin/python
from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler


def run(server_class=HTTPServer, handle_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handle_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run()
