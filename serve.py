#!/usr/bin/env python3
"""Static server with COOP/COEP for SharedArrayBuffer + multi-thread WASM."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import os

PORT = int(os.environ.get("PORT", "8080"))
DIR = os.path.dirname(os.path.abspath(__file__))


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

    def end_headers(self):
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        self.send_header("Cross-Origin-Resource-Policy", "cross-origin")
        # Allow CDN wasm/js modules
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()

    def guess_type(self, path):
        if path.endswith(".wasm"):
            return "application/wasm"
        return super().guess_type(path)


if __name__ == "__main__":
    os.chdir(DIR)
    httpd = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Serving {DIR}")
    print(f"Open http://127.0.0.1:{PORT}/")
    print("COOP/COEP enabled (SharedArrayBuffer OK)")
    httpd.serve_forever()
