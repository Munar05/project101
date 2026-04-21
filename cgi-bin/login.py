#!/usr/bin/env python3
print("Content-Type: text/html\n")

import cgi
import sqlite3

form = cgi.FieldStorage()
login = form.getvalue("login")
password = form.getvalue("pass")

conn = sqlite3.connect("users.db")
cur = conn.cursor()

cur.execute("SELECT * FROM users WHERE login=? AND password=?", (login, password))
user = cur.fetchone()

if user:
    print("<h2>Вход выполнен</h2>")
else:
    print("<h2>Неверный логин или пароль</h2>")

conn.close()