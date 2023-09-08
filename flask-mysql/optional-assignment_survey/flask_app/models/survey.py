from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    database = 'schema_surveys'

    def __init__(self, data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']

    @classmethod
    def read_all(cls):
        query = "SELECT * FROM surveys" #*CHANGE
        results = connectToMySQL(cls.database).query_db(query)
        
        all = []
        for row in results:
            all.append(cls(row))
        return all

    @classmethod
    def create(cls, data):
        query = """INSERT INTO surveys ( name, location, language, comment, created_at, updated_at )
                VALUES ( %(form_name)s, %(form_location)s, %(form_language)s, %(form_comment)s, NOW(), NOW() );"""
        return connectToMySQL(cls.database).query_db(query, data)

    # -------------------------------- validation -------------------------------- #
    @staticmethod
    def validate_survey(survey):
        is_valid = True

        if len(survey['form_name']) == 0:
            flash('Please enter a name.')
            is_valid = False
        if len(survey['form_name']) > 45:
            flash('Name must be less than 45 characters.')
            is_valid = False
        if len(survey['form_comment']) > 150:
            flash('Comment must be under 151 characters.')
            is_valid = False
        
        return is_valid