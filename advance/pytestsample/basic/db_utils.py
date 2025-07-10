# db_utils.py

import sqlite3

def init_db(conn):
    c = conn.cursor()
    c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
    conn.commit()

def add_user(conn, name):
    c = conn.cursor()
    c.execute("INSERT INTO users (name) VALUES (?)", (name,))
    conn.commit()

def get_users(conn):
    return conn.execute("SELECT * FROM users").fetchall()
