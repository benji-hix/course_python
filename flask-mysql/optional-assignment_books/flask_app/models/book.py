from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author, book

class Book: 
    database = 'schema_books'

    def __init__(self, data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.title = data['title']
        self.pages = data['pages']
        self.favorite_authors = []

    @classmethod
    def read_all(cls):
        query = "SELECT * FROM books"
        results = connectToMySQL(cls.database).query_db(query)
        
        all = []
        for row in results:
            all.append(cls(row))
        return all

    @classmethod
    def read(cls, pk):
        query = """SELECT * FROM books
                WHERE id = %(id)s;"""
        data = {'id': pk}
        results = connectToMySQL(cls.database).query_db(query, data)
        return results[0]

    @classmethod
    def create(cls, data):
        query = """INSERT INTO books (title, pages, created_at, updated_at ) 
                VALUES ( %(form_title)s, %(form_pages)s, NOW(), NOW() );"""
        return connectToMySQL(cls.database).query_db(query, data)

    @classmethod
    def create_favorite_book(cls, data):
        query = """INSERT INTO favorites (author_id, book_id )
                VALUES ( %(form_author_id)s, %(form_book_id)s );"""
        return connectToMySQL(cls.database).query_db(query, data)

    @classmethod
    def book_with_authors(cls, pk):
        query ="""SELECT * FROM books
                LEFT JOIN favorites
                ON books.id = favorites.book_id
                LEFT JOIN authors
                ON favorites.author_id = authors.id
                WHERE books.id = %(id)s"""
        data = { 'id': pk }
        results = connectToMySQL(cls.database).query_db(query, data)
        book = cls(results[0])

        for row in results:
            if row['authors.id'] == None:
                break
            author_data = {
                'id' : row['authors.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'created_at' : row['authors.created_at'],
                'updated_at' : row['authors.created_at']
            }
            book.favorite_authors.append( author.Author(author_data) )
            
        return book