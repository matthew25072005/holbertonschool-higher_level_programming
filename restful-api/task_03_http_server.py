import http.server
import json

PORT = 8000

class Handler(http.server.BaseHTTPRequestHandler):
    """Start of subclass"""

    def do_GET(self):
        # Handling the /status endpoint
        if self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "application/json")  # Change content-type to JSON
            self.end_headers()
            status = {
                "status": "OK"  # Return JSON response
            }
            self.wfile.write(json.dumps(status).encode("utf-8"))  # Send JSON response

        # Handling the /info endpoint
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode("utf-8"))

        # Handling the /data endpoint
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            sample_data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(sample_data).encode("utf-8"))

        # Handling the root endpoint
        elif self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # Handling undefined endpoints
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"404 Not Found")


# Set up and run the server
with http.server.HTTPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
