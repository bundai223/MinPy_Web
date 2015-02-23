#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
if sys.version_info < (3, 0, 0):
    # Python2系
    import SimpleHTTPServer as server
else:
    # Python3系
    import http.server as server

server.test(HandlerClass=server.SimpleHTTPRequestHandler)
