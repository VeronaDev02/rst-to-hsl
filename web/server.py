import os
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

PORT = 8080

os.chdir('D:/proj/video_stream_output')

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

with TCPServer(("", PORT), CORSRequestHandler) as httpd:
    print(f"Servidor rodando em> http://localhost:{PORT}")
    httpd.serve_forever()