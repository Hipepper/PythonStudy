from wsgiref.simple_server import make_server

module = __import__('pyramidapp')
application = getattr(module, 'app')
httpd = make_server('0.0.0.0', 8000, application)
print("Serving on port 8000...")

# Serve until process is killed
httpd.serve_forever()
