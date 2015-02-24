#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def run():
    import sys
    if sys.version_info < (3, 0, 0):
        # Python2系
        import SimpleHTTPServer as server
        server.test(HandlerClass=server.SimpleHTTPRequestHandler)
    else:
        # Python3系
        from http.server import HTTPServer, CGIHTTPRequestHandler
        host = 'localhost'
        port = 8000
        httpd = HTTPServer((host, port), CGIHTTPRequestHandler)
        print('serving at port', port)
        httpd.serve_forever()
