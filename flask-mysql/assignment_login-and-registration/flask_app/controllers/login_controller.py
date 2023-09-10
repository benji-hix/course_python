from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import login_model


@app.route('/')
def index():
    session['logged_in'] = False
    return render_template('index.html')

# ---------------------------------- register ---------------------------------- #
@app.route('/submit_register', methods = ['POST'])
def submit_registration():
    print(request.form['form_email'])
    if not login_model.Login.validate_registration(request.form):
        return redirect('/')
    register = login_model.Login.register(request.form)
    session['user_id'] = register
    redirect_url = '/welcome/' + str(session['user_id'])
    session['logged_in'] == True
    return redirect(redirect_url)

# ---------------------------------- log in ---------------------------------- #
@app.route('/submit_login', methods=['POST'])
def submit_login():
    if not login_model.Login.validate_login(request.form):
        return redirect('/')
    session['logged_in'] = True
    redirect_url = '/welcome/' + str(session['user_id'])
    return redirect(redirect_url)

# ------------------------- successful login redirect ------------------------ #
@app.route("/welcome/<int:user_id>")
def welcome(user_id):
    if not session['logged_in']:
        return redirect('/')
    login = login_model.Login.log_in(session['user_id'])
    session['user_name'] = login.first_name
    return render_template('welcome.html')


# ---------------------------------- log out --------------------------------- #
@app.route('/logout')
def log_out():
    session.clear()
    return redirect('/')