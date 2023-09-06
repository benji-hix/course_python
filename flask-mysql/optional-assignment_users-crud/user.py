from mysqlconnection import connectToMySQL

class User:
    user_database = 'schema_users'

    def __init__ (self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.user_database).query_db(query)

        all_users = []

        for row in results:
            all_users.append(cls(row))
        
        return all_users

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users ( first_name, last_name, email, created_at, updated_at ) VALUES ( %(form_first_name)s, %(form_last_name)s, %(form_email)s, NOW(), NOW() );"
        return connectToMySQL(cls.user_database).query_db(query, data)

    @classmethod
    def read(cls, user_id):
        query = """SELECT * FROM users
                WHERE id = %(id)s"""
        data = {'id': user_id}
        results = connectToMySQL(cls.user_database).query_db(query, data)
        return results[0]

    @classmethod
    def update(cls, data):
        query = """UPDATE users 
                SET first_name = %(form_first_name)s, last_name = %(form_last_name)s, email = %(form_email)s, updated_at = NOW() 
                WHERE id = %(form_id)s"""
        return connectToMySQL(cls.user_database).query_db(query, data)


    @classmethod
    def delete(cls, user_id):
        query = """DELETE FROM users
                WHERE id = %(id)s"""
        data = {"id": user_id}
        return connectToMySQL(cls.user_database).query_db(query, data)
