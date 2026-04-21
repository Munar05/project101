#!/usr/bin/env python3
print("Content-Type: text/html\n")

import cgi
import sqlite3

form = cgi.FieldStorage()
login = form.getvalue("login")
password = form.getvalue("pass")

conn = sqlite3.connect("users.db")
cur = conn.cursor()

# проверка — есть ли уже пользователь
cur.execute("SELECT * FROM users WHERE login=?", (login,))
user = cur.fetchone()

if user:
    print("<h2>Такой пользователь уже есть</h2>")
else:
    cur.execute("INSERT INTO users (login, password) VALUES (?, ?)", (login, password))
    conn.commit()
    print("<h2>Регистрация успешна</h2>")

conn.close()