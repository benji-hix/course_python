from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email: 
    database = 'schema_emails'

    def __init__(self, data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.email = data['email'] 

    @classmethod
    def read_all(cls):
        query = "SELECT * FROM emails"
        results = connectToMySQL(cls.database).query_db(query)
        
        all = []
        for row in results:
            all.append(cls(row))
        return all

    @classmethod
    def create(cls, data):
        query = """INSERT INTO emails ( email, created_at, updated_at )
                VALUES ( %(form_email)s, NOW(), NOW() );"""
        return connectToMySQL(cls.database).query_db(query, data)

    @staticmethod
    def validate_email(email):
        is_valid = True
        query = "SELECT * FROM emails WHERE email = %(form_email)s"
        unique_fail = connectToMySQL('schema_emails').query_db(query, email)


        if len(email['form_email']) == 0:
            flash("Please enter an email")
            is_valid = False
        elif not EMAIL_REGEX.match(email['form_email']):
            flash('Invalid email address')
            is_valid = False
        elif unique_fail:
            flash("Email already exists in database")
            is_valid = False
        return is_valid

    @classmethod
    def delete(cls, pk):
        query = """DELETE FROM emails
                WHERE id = %(id)s;"""
        data = {"id": pk}
        return connectToMySQL(cls.database).query_db(query, data)