#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
print("Content-Type: text/html; charset=utf-8\n")

import cgi
import sqlite3

form = cgi.FieldStorage()
items = form.getvalue("items")
total = form.getvalue("total")

conn = sqlite3.connect("users.db")
cur = conn.cursor()

cur.execute("INSERT INTO orders (items, total) VALUES (?, ?)", (items, total))
conn.commit()

conn.close()

print("OK")