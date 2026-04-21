#!/usr/bin/env python3
print("Content-Type: text/html\n")

import cgi

form = cgi.FieldStorage()
name = form.getvalue("name")

print("<h2>Заказ оформлен</h2>")
print("<p>Спасибо, " + str(name) + "</p>")