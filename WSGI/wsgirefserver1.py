from wsgiref.simple_server import make_server, demo_app


httpd = make_server('0.0.0.0', 8000, demo_app)
print("Serving on port 8000...")

# Serve until process is killed
httpd.serve_forever()
