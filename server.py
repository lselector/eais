#!/usr/bin/env python3
"""Simple HTTP server to serve the eAIs website on port 3000."""

import http.server
import socketserver
import os
import sys

PORT = 3000
WEBSITE_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'website'
)

# --------------------------------------------------------------
class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler to serve files from the website directory."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WEBSITE_DIR, **kwargs)

    def end_headers(self):
        """Add custom headers for better compatibility."""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header(
            'Access-Control-Allow-Methods', 'GET, POST, OPTIONS'
        )
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header(
            'Cache-Control', 'no-store, no-cache, must-revalidate'
        )
        super().end_headers()

    def log_message(self, format, *args):
        """Custom log format."""
        sys.stdout.write(
            "%s - [%s] %s\n" % (
                self.address_string(),
                self.log_date_time_string(),
                format % args
            )
        )

# --------------------------------------------------------------
def print_server_banner(port, directory):
    """Print server startup banner."""
    print("=" * 65)
    print("eAIs Website Server")
    print("=" * 65)
    print(f"Server running at: http://localhost:{port}")
    print(f"Serving files from: {directory}")
    print("=" * 65)
    print("Press Ctrl+C to stop the server")
    print("=" * 65)
    print()

# --------------------------------------------------------------
def handle_os_error(e, port):
    """Handle OS errors during server startup."""
    if e.errno == 48 or e.errno == 98:
        print(f"\nError: Port {port} is already in use.")
        print("Please stop the other process or use a different port.")
        sys.exit(1)
    else:
        raise

# --------------------------------------------------------------
def main():
    """Start the HTTP server."""
    try:
        if not os.path.exists(WEBSITE_DIR):
            print(f"Error: Website directory not found: {WEBSITE_DIR}")
            sys.exit(1)

        handler = CustomHTTPRequestHandler
        with socketserver.TCPServer(("", PORT), handler) as httpd:
            print_server_banner(PORT, WEBSITE_DIR)
            httpd.serve_forever()

    except KeyboardInterrupt:
        print("\n" + "=" * 65)
        print("Server stopped by user")
        print("=" * 65)
        sys.exit(0)
    except OSError as e:
        handle_os_error(e, PORT)
    except Exception as e:
        print(f"\nError starting server: {e}")
        sys.exit(1)

# --------------------------------------------------------------
if __name__ == "__main__":
    main()