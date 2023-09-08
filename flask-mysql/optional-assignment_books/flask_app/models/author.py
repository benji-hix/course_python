from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author, book

class Author: 
    database = 'schema_books' 

    def __init__(self, data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.first_name = data['first_name'] 
        self.last_name = data['last_name'] 
        self.favorite_books = []

    @classmethod
    def read_all(cls):
        query = "SELECT * FROM authors"
        results = connectToMySQL(cls.database).query_db(query)
        
        all = []
        for row in results:
            all.append(cls(row))
        return all

    @classmethod
    def read(cls, pk):
        query = """SELECT * FROM authors
                WHERE id = %(id)s;"""
        data = {'id': pk}
        results = connectToMySQL(cls.database).query_db(query, data)
        return results[0]

    @classmethod
    def create(cls, data):
        query = """INSERT INTO authors ( first_name, last_name, created_at, updated_at ) 
                VALUES ( %(form_first_name)s, %(form_last_name)s, NOW(), NOW() );""" 
        return connectToMySQL(cls.database).query_db(query, data)

    @classmethod
    def create_favorite_author(cls, data):
        query = """INSERT INTO favorites (author_id, book_id )
                VALUES ( %(form_author_id)s, %(form_book_id)s );"""
        return connectToMySQL(cls.database).query_db(query, data)

    @classmethod
    def author_with_books(cls, pk):
        query ="""SELECT * FROM authors
                LEFT JOIN favorites
                ON authors.id = favorites.author_id
                LEFT JOIN books 
                ON favorites.book_id = books.id
                WHERE authors.id = %(id)s"""
        data = { 'id': pk }
        results = connectToMySQL(cls.database).query_db(query, data)

        author = cls(results[0])

        for row in results:
            if row['books.id'] == None:
                break
            book_data = {
                'id' : row['books.id'],
                'title' : row['title'],
                'pages' : row['pages'],
                'created_at' : row['books.created_at'],
                'updated_at' : row['books.created_at']
            }
            author.favorite_books.append( book.Book(book_data) )
            
        return author