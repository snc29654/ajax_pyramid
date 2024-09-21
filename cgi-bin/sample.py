import cgi
import cgitb
import json
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


cgitb.enable()
form=cgi.FieldStorage()
data=form.getvalue("sent")
receive="receive data="+data
print("Content-type: text/html\n")
print(receive)
