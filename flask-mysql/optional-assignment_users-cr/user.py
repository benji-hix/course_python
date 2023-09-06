from mysqlconnection import connectToMySQL

class User:

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
        results = connectToMySQL('schema_users').query_db(query)

        all_users = []

        for row in results:
            all_users.append(cls(row))
        
        return all_users

    @classmethod
    def create(cls, data):
        print
        query = "INSERT INTO users ( first_name, last_name, email, created_at, updated_at ) VALUES ( %(form_first_name)s, %(form_last_name)s, %(form_email)s, NOW(), NOW() );"

        return connectToMySQL('schema_users').query_db(query, data)