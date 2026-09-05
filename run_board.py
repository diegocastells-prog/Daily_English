import sys
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HOST = "127.0.0.1"
PORT = 8000
PAGE = "project_dashboards.html"


def resource_root():
    if getattr(sys, "frozen", False):
        return Path(sys._MEIPASS)
    return Path(__file__).parent.resolve()


if __name__ == "__main__":
    root = resource_root()
    handler = lambda *args, **kwargs: SimpleHTTPRequestHandler(
        *args, directory=str(root), **kwargs
    )
    server = ThreadingHTTPServer((HOST, PORT), handler)
    print(f"Daily English dashboards: http://{HOST}:{PORT}/{PAGE}")
    print("Press Ctrl+C to stop the board server.")
    webbrowser.open(f"http://{HOST}:{PORT}/{PAGE}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nBoard server stopped.")
    finally:
        server.server_close()
