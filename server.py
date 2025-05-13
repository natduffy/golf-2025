from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser
import os
import subprocess
import sys
import json

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('.py'):
            try:
                # Get the script path
                script_path = self.path[1:]  # Remove leading slash
                
                # Run the Python script and capture output
                result = subprocess.run([sys.executable, script_path], 
                                     capture_output=True, 
                                     text=True)
                
                if result.returncode != 0:
                    raise Exception(f"Script failed with error: {result.stderr}")
                
                # Parse the output to separate headers and body
                output_lines = result.stdout.split('\n')
                headers = {}
                body_start = 0
                
                for i, line in enumerate(output_lines):
                    if line.strip() == '':
                        body_start = i + 1
                        break
                    if ':' in line:
                        key, value = line.split(':', 1)
                        headers[key.strip()] = value.strip()
                
                body = '\n'.join(output_lines[body_start:])
                
                # Validate JSON
                try:
                    json.loads(body)
                except json.JSONDecodeError:
                    raise Exception("Invalid JSON response from script")
                
                # Send response
                self.send_response(200)
                
                # Set headers from script output
                for key, value in headers.items():
                    self.send_header(key, value)
                
                # Ensure content type is set
                if 'Content-Type' not in headers:
                    self.send_header('Content-Type', 'application/json')
                
                self.end_headers()
                
                # Send the body
                self.wfile.write(body.encode())
                
            except Exception as e:
                # Send error response as JSON
                error_response = {
                    'status': 'error',
                    'message': str(e)
                }
                
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps(error_response).encode())
        else:
            # Handle regular files as before
            super().do_GET()

def run(server_class=HTTPServer, handler_class=CustomHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    
    # Open the browser automatically in development
    if os.environ.get('ENVIRONMENT') != 'production':
        webbrowser.open(f'http://localhost:{port}')
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.server_close()

if __name__ == '__main__':
    run() 