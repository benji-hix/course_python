from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import login_model


@app.route('/')
def index():
    session['logged_in'] = False
    return render_template('index.html')

# ------------------- submit register attempt, then log in ------------------- #
@app.route('/submit_register', methods = ['POST'])
def submit_registration():
    session['form_first_name'] = request.form['form_first_name']
    session['form_last_name'] = request.form['form_last_name']
    session['form_email'] = request.form['form_email']
    session['form_password'] = request.form['form_password']
    if not login_model.Login.validate_registration(request.form):
        return redirect('/')
    register = login_model.Login.register(request.form)
    session['user_id'] = register
    session['logged_in'] = True
    redirect_url = '/welcome/' + str(session['user_id'])
    return redirect(redirect_url)

# --------------------------- submit log in attempt -------------------------- #
@app.route('/submit_login', methods=['POST'])
def submit_login():
    session['form_email'] = request.form['form_email']
    session['form_password'] = request.form['form_password']
    if not login_model.Login.validate_login(request.form):
        return redirect('/')
    session['logged_in'] = True
    redirect_url = '/welcome/' + str(session['user_id']) #! session['user_id] is set by validate_login
    return redirect(redirect_url)

#! ------------------------- user homepage redirect ------------------------ #
@app.route("/welcome/<int:user_id>")
def welcome(user_id):
    if not session['logged_in']:
        return redirect('/')
    login = login_model.Login.log_in(session['user_id'])
    session['user_name'] = login.first_name
    all_messages = login_model.Login.read_messages()
    sent_messages = login_model.Login.read_sent_messages()
    all_logins = login_model.Login.read_logins()
    receive_count = login_model.Login.read_message_receive_count()
    sent_count = login_model.Login.read_message_sent_count()
    return render_template('welcome.html', all_messages = all_messages, all_logins=all_logins, 
        receive_count=receive_count, sent_count=sent_count, sent_messages=sent_messages)


# ---------------------------------- log out --------------------------------- #
@app.route('/logout')
def log_out():
    session.clear()
    return redirect('/')

# ------------------------------ delete message ------------------------------ #
@app.route('/delete/<int:pk>')
def delete_message(pk):
    login_model.Login.delete_message(pk)
    redirect_url = '/welcome/' + str(session['user_id'])
    return redirect(redirect_url)

# ---------------------------- submit new message ---------------------------- #
@app.route('/submit_message', methods=['POST'])
def submit_message():
    login_model.Login.create_message(request.form)
    redirect_url = '/welcome/' + str(session['user_id'])
    return redirect(redirect_url)