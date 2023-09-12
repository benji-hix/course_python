from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app_database, app, bcrypt
from flask import flash, session

import re
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:

    def __init__(self, data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']

#* ----------------------------- validate register ---------------------------- #
    @staticmethod
    def validate_register(form): 
        # preserve text input fields
        session['form_first_name'] = form['form_first_name']
        session['form_last_name'] = form['form_last_name']
        session['form_email'] = form['form_email']
        session['form_password'] = form['form_password']

        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s"
        data = { 'email': form['form_email']}
        unique_fail = connectToMySQL(app_database).query_db(query, data) #! make sure app_database is defined

        # blank forms 
        if len(form['form_first_name']) < 1 or len(form['form_last_name']) < 1 or len(form['form_email']) < 1:
            flash('Please complete all fields of entry', 'register')
            is_valid = False
        elif len(form['form_first_name']) < 1 or len(form['form_last_name']) < 1:
            flash('First name and Last name must be at least 2 characters long', 'register')
            is_valid = False

        # email validate
        elif not email_regex.match(form['form_email']):
            flash('Invalid email address', 'register')
            is_valid = False
        elif unique_fail:
            flash('Email already exists in database', 'register') 
            is_valid = False

        # passwords don't match
        elif form['form_password'] != form['form_confirm_password']:
            flash('Passwords do not match', 'register')
            is_valid = False
        # password must have at least 1 uppercase and 1 number
        elif not (any(char.isdigit() for char in form['form_password']) 
        and any(char.isupper() for char in form['form_password']) 
        and len(form['form_password']) >= 8):
            flash('Password must be at least 8 characters and contain at least one uppercase letter and one number', 'register')
            is_valid = False
        return is_valid 

#* ------------------------------ validate login ------------------------------ #
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
        # check if email exists in database
        query = "SELECT * FROM users WHERE email = %(email)s"
        data = { 'email': form['form_email']}
        found_user = connectToMySQL(app_database).query_db(query, data)
        print(found_user)
        if len(found_user) < 1:
            flash ('Invalid email/password', 'login')
            is_valid = False
            return is_valid
        # check password
        found_user = found_user[0]
        if not bcrypt.check_password_hash(found_user['password'], form['form_password']):
            flash ('Invalid email/password', 'login')
            is_valid = False
        # update session
        if is_valid:
            session['user_id'] = found_user['id']
            session['logged_in'] = True
        return is_valid

#~ ---------------------------------- register ---------------------------------- #
    @classmethod
    def register(cls, form):
        password_hash = bcrypt.generate_password_hash(form['form_password'])
        query = """INSERT INTO users ( first_name, last_name, email, password, created_at, updated_at ) #! table name + values
                VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW() );"""
        data = { 
            'first_name' : form['form_first_name'],
            'last_name' : form['form_last_name'],
            'email' : form['form_email'],
            'password' : password_hash
            }
        session['logged_in'] = True
        return connectToMySQL(app_database).query_db(query, data)

#~ --------------------------------- log in  --------------------------------- #
    @classmethod
    def login(cls, pk):
        query = """SELECT * FROM users
                WHERE id = %(id)s;"""
        data = {'id': pk}
        results = connectToMySQL(app_database).query_db(query, data)
        return cls(results[0])