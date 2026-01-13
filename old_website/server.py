#!/usr/bin/env python3
"""
Simple HTTP server to serve the eAIs static website on port 3000.

Usage:
    python server.py
    
Then open your browser to: http://localhost:3000
"""

import http.server
import socketserver
import os
import sys

# Configuration
PORT = 3000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler to serve files from the website directory."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        """Add custom headers for better compatibility."""
        # Add CORS headers for local development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        # Cache control
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()
    
    def log_message(self, format, *args):
        """Custom log format."""
        sys.stdout.write("%s - [%s] %s\n" %
                        (self.address_string(),
                         self.log_date_time_string(),
                         format % args))

def main():
    """Start the HTTP server."""
    try:
        # Change to the website directory
        os.chdir(DIRECTORY)
        
        # Create the server
        with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
            print("=" * 70)
            print(f"eAIs Website Server")
            print("=" * 70)
            print(f"Server running at: http://localhost:{PORT}")
            print(f"Serving files from: {DIRECTORY}")
            print("=" * 70)
            print("Press Ctrl+C to stop the server")
            print("=" * 70)
            print()
            
            # Start serving
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n" + "=" * 70)
        print("Server stopped by user")
        print("=" * 70)
        sys.exit(0)
    except OSError as e:
        if e.errno == 48 or e.errno == 98:  # Address already in use
            print(f"\nError: Port {PORT} is already in use.")
            print("Please stop the other process or use a different port.")
            sys.exit(1)
        else:
            raise
    except Exception as e:
        print(f"\nError starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
