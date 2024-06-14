import os
import sqlite3
from helpers import execute_query, fetch_all, fetch_one

DB_FILES = 'books_library.db'

class Category:
    @staticmethod
    def create_table():
        execute_query('''
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL
            )
        ''')

    @staticmethod
    def create(title):
        execute_query('INSERT INTO categories (title) VALUES (?)', (title,))
        category_id = fetch_one('SELECT last_insert_rowid()')[0]
        return category_id

    @staticmethod
    def delete(category_id):
        execute_query('DELETE FROM categories WHERE id = ?', (category_id,))

    @staticmethod
    def get_all():
        return fetch_all('SELECT * FROM categories')

class Book:
    @staticmethod
    def drop_table():
        execute_query('DROP TABLE IF EXISTS books')

    @staticmethod
    def create_table():
        execute_query('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                publishyear REAL NOT NULL,
                category_id INTEGER,
                category_title TEXT NOT NULL,
            
                FOREIGN KEY (category_id) REFERENCES categories(id),
                FOREIGN KEY (category_title) REFERENCES categories(title)
            )
        ''')

    @staticmethod
    def create(title, author, publishyear, category_id,category_title):
        execute_query('INSERT INTO books (title, author, publishyear, category_id,category_title) VALUES (?, ?, ?, ?, ?)', (title, author, publishyear, category_id, category_title))
        book_id = fetch_one('SELECT last_insert_rowid()')[0]
        return book_id

    @staticmethod
    def delete(book_id):
        execute_query('DELETE FROM books WHERE id = ?', (book_id,))

    @staticmethod
    def get_all():
        return fetch_all('SELECT * FROM books')


    @staticmethod
    def get_by_category_id(category_id):
        return fetch_all('SELECT * FROM books WHERE category_id = ?', (category_id,))
    @staticmethod
    def get_by_category_title(category_title):
        return fetch_all('SELECT * FROM books WHERE category_title = ?', (category_title,))


# Create database and tables if they don't exist
if not os.path.exists(DB_FILES):
    conn = sqlite3.connect(DB_FILES)
    conn.close()

Category.create_table()
Book.drop_table()
Book.create_table()