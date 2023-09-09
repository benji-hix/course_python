from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:

    database = 'schema_dojos_and_ninjas'

    def __init__(self, data):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = """INSERT INTO ninjas ( dojo_id, first_name, last_name, age, created_at, updated_at ) 
                VALUES ( %(form_dojo_id)s, %(form_first_name)s, %(form_last_name)s, %(form_age)s, NOW(), NOW() );"""
        return connectToMySQL(cls.database).query_db(query, data)