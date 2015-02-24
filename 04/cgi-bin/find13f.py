#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
from datetime import datetime


html_body = """
<html><head>
<meta http-equiv="content-type" content="text/html;charset=utf-8"> </head>
<body>
%s
</body>
</html>"""

content = ''
form = cgi.FieldStorage()
year_str = form.getvalue('year', '')

if not year_str.isdigit():            # (1)
    content = "西暦を入力してください"
else:
    year = int(year_str)
    friday13 = []

    for month in range(1, 13):
        date = datetime(year, month, 13)
        if date.weekday() == 4:
            friday13.append(month)

    if 0 < len(friday13):                      # (2)
        content = "%d年には合計%d個の13日の金曜日があります。<br>" % (year, len(friday13))
        for month in friday13:
            content += "  %d月<br>" % month
    else:
        content = "%d年には13日の金曜日がありません。" % year

print("Content-type: text/html;charset=utf-8\n")
print((html_body % content))
