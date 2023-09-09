from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    database = 'schema_dojos_and_ninjas'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_ninjas = []


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

    @classmethod
    def get_dojo_with_ninjas( cls , pk ):
        query = """SELECT * 
                FROM dojos 
                LEFT JOIN ninjas 
                ON dojos.id = ninjas.dojo_id
                WHERE dojos.id = %(id)s;"""
        data = { 'id': pk }
        results = connectToMySQL(cls.database).query_db( query , data )
        
        dojo = cls( results[0] )

        for row in results:
            if row['ninjas.id'] == None:
                break
            ninja_data = {
                "id" : row["ninjas.id"],
                "first_name" : row["first_name"],
                "last_name" : row["last_name"],
                "age" : row["age"],
                "created_at" : row["ninjas.created_at"],
                "updated_at" : row["ninjas.updated_at"]
            }
            dojo.dojo_ninjas.append( ninja.Ninja( ninja_data ) )

        return dojo