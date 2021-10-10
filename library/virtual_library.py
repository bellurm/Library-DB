import sqlite3
import time

class Book():
    def __init__(self, name, author, publisher, category, page):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.category = category
        self.page = page

    def __str__(self):
        return "Book Name: {}\nAuthor: {}\nPublisher: {}\nCategory: {}\nPage: {}\n".format(self.name, self.author, self.publisher, self.category, self.page)

class Library():
    def __init__(self):
        self.create_connection()
    def create_connection(self):
        self.connection = sqlite3.connect("VirtualLibrary.db")
        self.cursor = self.connection.cursor()

        query = "CREATE TABLE IF NOT EXISTS books (name TEXT, author TEXT, publisher TEXT, category TEXT, pages INT)"
        self.cursor.execute(query)
        self.connection.commit()

    def disconnect(self):
        self.connection.close()

    def show_the_books(self):
        query = "SELECT * FROM books"
        self.cursor.execute(query)
        books = self.cursor.fetchall()

        if (len(books) == 0):
            print("[*] There are no books in the library!")
        else:
            for i in books:
                book = Book(i[0], i[1], i[2], i[3], i[4])
                print(book)

    def query_book(self, name):
        query = "SELECT * FROM books WHERE name = ?"
        self.cursor.execute(query, (name,))
        books = self.cursor.fetchall()

        if (len(books) == 0):
            print("There is no such book!")
        else:
            book = Book(books[0][0], books[0][1], books[0][2], books[0][3], books[0][4])
            print(book)

    def add_book(self, book):
        query = "INSERT INTO books VALUES(?,?,?,?,?)"
        self.cursor.execute(query, (book.name, book.author, book.publisher, book.category, book.page))
        self.connection.commit()

    def delete_book(self, name):
        query = "DELETE FROM books WHERE name = ?"
        self.cursor.execute(query, (name,))
        self.connection.commit()
