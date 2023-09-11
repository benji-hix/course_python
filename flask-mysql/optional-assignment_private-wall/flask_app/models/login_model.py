from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app_database, app, bcrypt
from flask import flash, session

import re
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Login: 

    def __init__(self, data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.first_name = data['first_name'] 
        self.last_name = data['last_name'] 
        self.email = data['email']

# --------------------------------- validate --------------------------------- #
    @staticmethod
    def validate_registration(form): 
        is_valid = True
        query = "SELECT * FROM logins WHERE email = %(email)s"
        data = { 'email': form['form_email']}
        unique_fail = connectToMySQL(app_database).query_db(query, data)

        # blank forms 
        if len(form['form_first_name']) < 1 or len(form['form_last_name']) < 1 or len(form['form_email']) < 1:
            flash('Please complete all fields of entry', 'register')
            is_valid = False
        if len(form['form_first_name']) < 1 or len(form['form_last_name']) < 1:
            flash('First name and Last name must be at least 3 characters long', 'register')
            is_valid = False

        # email validate
        elif not email_regex.match(form['form_email']):
            flash('Invalid email address', 'register')
            is_valid = False
        elif unique_fail:
            flash('Email already exists in database', 'reguster') 
            is_valid = False

        # passwords don't match
        elif form['form_password'] != form['form_pswd_confirm']:
            flash('Passwords do not match', 'register')
            is_valid = False
        # password must have at least 1 uppercase and 1 number
        elif not (any(char.isdigit() for char in form['form_password']) and any(char.isupper() for char in form['form_password']) and len(form['form_password']) >= 8):
            flash('Password must be at least 8 characters and contain at least one uppercase letter and one number', 'register')
            is_valid = False
        return is_valid 

    @staticmethod
    def validate_login(form):
        is_valid = True

        # blank forms 
        if len(form['form_password']) < 1 or len(form['form_email']) < 1:
            flash('Please complete all fields of entry', 'login')
            is_valid = False
            return is_valid
        elif not email_regex.match(form['form_email']):
            flash('Invalid email address', 'login')
            is_valid = False
            return is_valid

        query = "SELECT * FROM logins WHERE email = %(form_email)s"
        data = { 'email': form['form_email']}
        found_user = connectToMySQL(app_database).query_db(query, form)
        print(found_user)
        if len(found_user) < 1:
            flash ('Invalid email/password', 'login')
            is_valid = False
            return is_valid
        found_user = found_user[0]
        if not bcrypt.check_password_hash(found_user['password'], form['form_password']):
            flash ('Invalid email/password', 'login')
            is_valid = False
        if is_valid:
            session['user_id'] = found_user['id']
        return is_valid

    
# --------------------------------- log in  --------------------------------- #
    @classmethod
    def log_in(cls, pk):
        query = """SELECT * FROM logins
                WHERE id = %(id)s;"""
        data = {'id': pk}
        results = connectToMySQL(app_database).query_db(query, data)
        return cls(results[0])


# ---------------------------------- register ---------------------------------- #
    @classmethod
    def register(cls, form):
        encrypted_password = bcrypt.generate_password_hash(form['form_password'])
        query = """INSERT INTO logins ( first_name, last_name, email, password, created_at, updated_at ) 
                VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW() );"""
        data = { 
            'first_name' : form['form_first_name'],
            'last_name' : form['form_last_name'],
            'email' : form['form_email'],
            'password' : encrypted_password
            }
        return connectToMySQL(app_database).query_db(query, data)


# ------------------------------ read all logins ----------------------------- #
    @classmethod
    def read_logins(cls):
        query = "SELECT * FROM logins ORDER BY first_name"
        results = connectToMySQL(app_database).query_db(query)
        all = []
        for row in results:
            all.append(cls(row))
        return all

# -------------------------- read received messages -------------------------- #
    @classmethod
    def read_messages(cls):
        query = """
        SELECT content, concat(sender.first_name, ' ', sender.last_name) AS sender_name, 
        messages.id as message_id FROM logins
        LEFT JOIN messages on logins.id = messages.receiver_id
        LEFT JOIN logins AS sender ON messages.sender_id = sender.id
        WHERE messages.receiver_id = %(user_id)s
        """
        data = {'user_id' : session['user_id'] }
        return connectToMySQL(app_database).query_db(query, data)

# ---------------------------- read sent messages ---------------------------- #
    @classmethod
    def read_sent_messages(cls):
        query = """
        SELECT content, concat(receiver.first_name, ' ', receiver.last_name) AS receiver_name, 
        messages.id as message_id FROM logins
        LEFT JOIN messages on logins.id = messages.sender_id
        LEFT JOIN logins AS receiver ON messages.receiver_id = receiver.id
        WHERE messages.sender_id = %(user_id)s
        """
        data = {'user_id' : session['user_id'] }
        return connectToMySQL(app_database).query_db(query, data)
# ------------------------ read receive message count ----------------------- #
    @classmethod
    def read_message_receive_count(cls):
        query = """
        SELECT count(messages.id) AS receive_count FROM messages
        WHERE messages.receiver_id = %(receiver_id)s
        """
        data = { 'receiver_id' : session['user_id'] }
        receive_number = connectToMySQL(app_database).query_db(query, data)[0]
        return receive_number

# ------------------------ read sent message count ----------------------- #
    @classmethod
    def read_message_sent_count(cls):
        query = """
        SELECT count(messages.id) AS sent_count FROM messages
        WHERE messages.sender_id = %(sender_id)s
        """
        data = { 'sender_id' : session['user_id'] }
        sent_number = connectToMySQL(app_database).query_db(query, data)[0]
        return sent_number

# ------------------------------ create messages ----------------------------- #
    @classmethod
    def create_message(cls, form):
        query = """
        INSERT INTO messages (content, created_at, sender_id, receiver_id)
        VALUES (%(content)s, NOW(), %(sender_id)s, %(receiver_id)s);
        """
        data = {
            'content' : form['form_content'],
            'sender_id' : session['user_id'],
            'receiver_id' : form['form_receiver_id']
        }
        return connectToMySQL(app_database).query_db(query, data)

    # ------------------------------ delete message ------------------------------ #
    @classmethod
    def delete_message(cls, pk):
        query = """
        DELETE FROM messages
        WHERE id = %(message_id)s
        """
        data = { 'message_id' : pk }
        return connectToMySQL(app_database).query_db(query, data)