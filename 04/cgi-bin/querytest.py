#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi


html_body = """<head><body>
foo = %s
</body></head>"""

form = cgi.FieldStorage()
print("Content-type: text/html\n")
print(html_body % form.getvalue('foo', 'N/A'))
