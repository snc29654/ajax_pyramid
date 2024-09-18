#!/〇〇/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import json

cgitb.enable()
form=cgi.FieldStorage()
data=form.getvalue("sent")
receive=data+"OK"
print("Content-type: text/html\n")
print(receive)
