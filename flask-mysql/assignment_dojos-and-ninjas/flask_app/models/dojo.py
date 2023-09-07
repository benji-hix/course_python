from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    database = 'schema_dojos_and_ninjas'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # @classmethod
    # def (cls):
    # connectToMySQL(cls.main_database).query_db(query)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.database).query_db(query)

        all_dojos = []

        for row in results:
            all_dojos.append(cls(row))
        
        return all_dojos

    @classmethod
    def read(cls, dojo_id):
        query = """SELECT * FROM dojos
                WHERE id = %(id)s;"""
        data = { 'id': dojo_id }
        results = connectToMySQL(cls.database).query_db(query, data)
    
        return results[0]

    @classmethod
    def create(cls, data):
        query = """INSERT INTO dojos ( name, created_at, updated_at ) 
                VALUES ( %(form_name)s, NOW(), NOW() );"""
        return connectToMySQL(cls.database).query_db(query, data)
