#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
print("Content-Type: text/html; charset=utf-8\n")

import sqlite3

conn = sqlite3.connect("users.db")
cur = conn.cursor()

cur.execute("SELECT * FROM orders ORDER BY id DESC")
rows = cur.fetchall()

for r in rows:
    print("<div style='padding:10px;border:1px solid #ccc;margin:5px;'>")
    print("<b>ID:</b>", r[0], "<br>")
    print("<b>Товары:</b>", r[1], "<br>")
    print("<b>Сумма:</b>", r[2], "₸<br>")
    print("<b>Дата:</b>", r[3])
    print("</div>")

conn.close()