#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
print("Content-Type: text/html; charset=utf-8\n")

import cgi

form = cgi.FieldStorage()
name = form.getvalue("name")

print("<h2>Заказ оформлен</h2>")
print("<p>Спасибо, " + str(name) + "</p>")