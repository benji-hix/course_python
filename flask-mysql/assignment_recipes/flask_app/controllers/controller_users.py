from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import model_recipe, model_user

@app.route('/')
def index():
    session['logged_in'] = False
    return render_template('access.html')

# ------------- submit register attempt, validate, create, log in ------------ #
@app.route('/submit-register', methods = ['POST'])
def submit_register():
    #* validate
    if not model_user.User.validate_register(request.form): 
        return redirect('/')
    #~ create login
    register = model_user.User.register(request.form) #! register should change logged_in session variable
    session['user_id'] = register
    #redirect
    return redirect('/recipes')

# ------------------ submit log-in attempt, validate, log in ----------------- #
@app.route('/submit-login', methods=['POST'])
def submit_login():
    # preserve text input fields
    session['form_email'] = request.form['form_email']
    session['form_password'] = request.form['form_password']
    #* validate
    if not model_user.User.validate_login(request.form):
        return redirect('/')
    # redirect
    return redirect('/recipes')


# ---------------------------------- log out --------------------------------- #
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')