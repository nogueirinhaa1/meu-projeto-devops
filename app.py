# app.py
from http.server import HTTPServer, BaseHTTPRequestHandler

def main():
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"OK")

    server = HTTPServer(("0.0.0.0", 8000), Handler)
    print("Server running on http://0.0.0.0:8000")
    server.serve_forever()

if __name__ == "__main__":
    main()
