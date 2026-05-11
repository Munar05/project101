#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("Content-Type: text/html; charset=utf-8\n")

import sqlite3

conn = sqlite3.connect("users.db")
cur = conn.cursor()

cur.execute("DELETE FROM orders")

conn.commit()
conn.close()

print("OK")