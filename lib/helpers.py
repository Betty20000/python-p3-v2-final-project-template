import sqlite3

def execute_query(query, parameters=()):
    conn = sqlite3.connect('books_library.db')
    cur = conn.cursor()
    cur.execute(query, parameters)
    conn.commit()
    conn.close()

def fetch_all(query, parameters=()):
    conn = sqlite3.connect('books_library.db')
    cur = conn.cursor()
    cur.execute(query, parameters)
    result = cur.fetchall()
    conn.close()
    return result

def fetch_one(query, parameters=()):
    conn = sqlite3.connect('books_library.db')
    cur = conn.cursor()
    cur.execute(query, parameters)
    result = cur.fetchone()
    conn.close()
    return result