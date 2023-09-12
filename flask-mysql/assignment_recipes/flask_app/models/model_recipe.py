from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app_database, app, bcrypt
from flask_app.models import model_recipe, model_user
from flask import flash, session

import re
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Recipe:

    def __init__(self, data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date = data['date']
        self.under_30 = data['under_30']
        self.user_id = data['user_id']
        self.recipe_list = []

# ------------------------------ validate recipe ----------------------------- #
    @staticmethod
    def validate_recipe(form):
        is_valid = True

        # blank forms 
        if len(form['form_name']) < 1:
            flash('Please complete name field', 'recipe')
            is_valid = False
        elif len(form['form_description']) < 1:
            flash('Please complete description field', 'recipe')
            is_valid = False
        elif len(form['form_instructions']) < 1:
            flash('Please complete instructions field', 'recipe')
            is_valid = False
        elif len(form['form_date']) < 1:
            flash('Please complete date field', 'recipe')
            is_valid = False
        elif len(form['form_under_30']) < 1:
            flash('Please indicate if recipe requires less than 30 minutes', 'recipe')
            is_valid = False

        elif len(form['form_name']) < 3:
            flash('Name must be at least 3 characters in length', 'recipe')
            is_valid = False
        elif len(form['form_description']) < 3:
            flash('Description must be at least 3 characters in length', 'recipe')
            is_valid = False
        elif len(form['form_instructions']) < 3:
            flash('Instructions must be at least 3 characters in length', 'recipe')
            is_valid = False
        
        return is_valid


# ---------------------------------- create recipe ---------------------------------- #
    @classmethod
    def create_recipe(cls, form):
        query = """
        INSERT INTO recipes ( name, description, instructions, date, under_30, user_id, created_at, updated_at )
        VALUES ( %(name)s, %(description)s, %(instructions)s, %(date)s, %(under_30)s, %(user_id)s, NOW(), NOW() );
        """
        data = {
            'name' : form['form_name'],
            'description' : form['form_description'],
            'instructions' : form['form_instructions'],
            'date' : form['form_date'],
            'under_30' : form['form_under_30'],
            'user_id' : session['user_id']
        }
        return connectToMySQL(app_database).query_db(query, data)

# -------------------------------- update recipe -------------------------------- #
    @classmethod
    def update_recipe(cls, form):
        query = """UPDATE recipes 
                SET name = %(name)s, description = %(description)s, instructions = %(instructions)s,
                date = %(date)s, under_30 = %(under_30)s, updated_at = NOW() 
                WHERE id = %(id)s;"""
        data = {
            'name' : form['form_name'],
            'description' : form['form_description'],
            'instructions' : form['form_instructions'],
            'date' : form['form_date'],
            'under_30' : form['form_under_30'],
            'id' : form['form_id']
        }
        return connectToMySQL(app_database).query_db(query, data)

# ------------------------------- read one recipe ------------------------------- #
    @classmethod
    def read_recipe(cls, pk):
        query = """SELECT * FROM recipes
                LEFT JOIN users on recipes.user_id = users.id
                WHERE recipes.id = %(id)s;
                """
        data = {'id': pk}
        results = connectToMySQL(app_database).query_db(query, data)
        session['first_name'] = results[0]['first_name']
        session['name'] = results[0]['name']
        session['description'] = results[0]['description']
        session['instructions'] = results[0]['instructions']
        session['date'] = results[0]['date']
        session['id'] = results[0]['id']
        session['under_30'] = results[0]['under_30']
        return cls(results[0])

# ----------------------------- read all recipes ----------------------------- #
    @classmethod
    def read_recipes_with_user(cls):
        query = """SELECT *, recipes.id as this_recipe
                FROM recipes
                LEFT JOIN users on recipes.user_id = users.id 
                """

        return connectToMySQL(app_database).query_db(query)

# ------------------------------ delete ??? ------------------------------ #
    @classmethod
    def delete_recipe(cls, pk):
        query = """
        DELETE FROM recipes
        WHERE id = %(id)s;
        """
        data = { 'id' : pk }
        return connectToMySQL(app_database).query_db(query, data)

# --------------------------- clear recipe session --------------------------- #   \
    @classmethod
    def clear_recipe_session(cls):
        session['first_name'] = ''
        session['name'] = ''
        session['description'] = ''
        session['instructions'] = ''
        session['date'] = ''
        session['id'] = ''
        session['under_30'] = ''