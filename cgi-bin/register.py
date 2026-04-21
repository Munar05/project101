#!/usr/bin/env python3
print("Content-Type: text/html\n")

import cgi
import sqlite3

form = cgi.FieldStorage()
login = form.getvalue("login")
password = form.getvalue("pass")

conn = sqlite3.connect("users.db")
cur = conn.cursor()

cur.execute("SELECT * FROM users WHERE login=?", (login,))
user = cur.fetchone()

if user:
    print("<h2>Такой пользователь уже есть</h2>")
else:
    cur.execute("INSERT INTO users (login, password) VALUES (?, ?)", (login, password))
    conn.commit()

    # 👉 редирект в login.html
    print("""
    <script>
        alert('Регистрация успешна!');
        window.location.href = '/login.html';
    </script>
    """)

conn.close()