#!/usr/bin/python3
"""
This script sets up a basic HTTP server using the http.server module.
It handles GET requests, serves JSON data for specific endpoints,
and handles errors for undefined endpoints.
"""

import http.server
import socketserver
import json

class MyHandler(http.server.BaseHTTPRequestHandler):
    """Request handler class for our HTTP server."""

    def do_GET(self):
        """
        Handle GET requests based on the requested path.

        Endpoints:
        - /: Returns a simple text message.
        - /data: Returns a sample JSON dataset.
        - /status: Returns a JSON response with the API status.
        Any other endpoint will return a 404 error.
        """
        if self.path == "/":
            # Root path: simple text response
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            # /data path: return a sample JSON dataset
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode())

        elif self.path == "/status":
            # /status path: return a JSON status message
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            # Cambiar la respuesta de estado
            status = {
                "status": "success"
            }
            self.wfile.write(json.dumps(status).encode())

        else:
            # Undefined paths: return a 404 error
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

# Define the server port
PORT = 8000

# Set up the server using MyHandler to handle requests
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving on port {PORT}")
    # Start the server, keeping it running forever
    httpd.serve_forever()
