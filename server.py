import http.server
import socketserver
import os

PORT = 8769

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Allow requests to root
        if self.path == '/':
            self.path = '/index.html'
        else:
            # Map clean URLs to .html
            path_parts = self.path.split('/')
            last_part = path_parts[-1]
            if not '.' in last_part and '?' not in last_part and self.path != '/':
                path_with_html = self.path + '.html'
                if os.path.exists('.' + path_with_html):
                    self.path = path_with_html
        return super().do_GET()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
