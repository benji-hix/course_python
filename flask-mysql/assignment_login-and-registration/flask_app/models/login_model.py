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
        unique_fail = connectToMySQL('schema_logins').query_db(query, data)

        # blank forms 
        if len(form['form_first_name']) < 1 or len(form['form_last_name']) < 1 or len(form['form_email']) < 1:
            flash('Please complete all fields of entry', 'register')
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
        elif not (any(char.isdigit() for char in form['form_password']) and any(char.isupper() for char in form['form_password'])):
            flash('Password must contain at least one uppercase letter and one number', 'register')
            is_valid = False
        return is_valid 

    @staticmethod
    def validate_login(form):
        is_valid = True
        query = "SELECT * FROM logins WHERE email = %(form_email)s"
        found_user = connectToMySQL(app_database).query_db(query, form)
        found_user = found_user[0]

        if len(form['form_email']) < 1:
            flash('Please enter an email', 'login')
            is_valid = False
        elif len(found_user) < 1:
            flash ('Email not found in database', 'login')
            is_valid = False
        elif not bcrypt.check_password_hash(found_user['password'], form['form_password']):
            flash ('Invalid password', 'login')
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
        return connectToMySQL('schema_logins').query_db(query, data)

