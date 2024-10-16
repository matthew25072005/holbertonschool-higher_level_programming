#!/usr/bin/python3

import http.server
import json

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        """Handle GET requests"""
        if self.path == '/':
            # Maneja la ruta raíz '/'
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            response_message = "Hello, this is a simple API!"
            self.wfile.write(response_message.encode())

        elif self.path == '/data':
            # Maneja la ruta '/data' para devolver JSON
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())

        elif self.path == '/status':
            # Maneja la ruta '/status' para verificar el estado del API
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            status = {"status": "OK"}
            self.wfile.write(json.dumps(status).encode())

        else:
            # Maneja cualquier otra ruta no definida
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_message = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error_message).encode())

if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("Server running on port 8000...")
    httpd.serve_forever()
