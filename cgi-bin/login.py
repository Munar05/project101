#!/usr/bin/env python3
print("Content-Type: text/html\n")

import cgi
import sqlite3

form = cgi.FieldStorage()

login = form.getvalue("login")
password = form.getvalue("pass")

# защита от пустых значений
if not login or not password:
    print("""
    <script>
        alert('Введите логин и пароль!');
        window.location.href = '/login.html';
    </script>
    """)
    exit()

conn = sqlite3.connect("users.db")
cur = conn.cursor()

cur.execute(
    "SELECT * FROM users WHERE login=? AND password=?",
    (login, password)
)

user = cur.fetchone()

if user:
    print("""
    <script>
        alert('Добро пожаловать!');
        window.location.href = '/index.html';
    </script>
    """)
else:
    print("""
    <script>
        alert('Неверный логин или пароль!');
        window.location.href = '/login.html';
    </script>
    """)

conn.close()