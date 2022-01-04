from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/greetings':
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(bytes(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "utf8"))
        else:
            self.send_response(400)
            self.send_header('Content-type','text/html')
            self.end_headers()

            message = "Invalid endpoint"
            self.wfile.write(bytes(message, "utf8"))

with HTTPServer(('', 8181), handler) as server:
    server.serve_forever()

