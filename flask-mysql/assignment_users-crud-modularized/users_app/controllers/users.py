from users_app import app
from flask import render_template, redirect, request, session, flash
from users_app.models.user import User

@app.route('/users')
def index():

    all_users = User.get_all()
    return render_template('read.html', all_users = all_users)

@app.route('/users/new')
def users_create():
    input_phrase = 'Add A New User'
    return render_template('create.html', input_phrase = input_phrase)

@app.route('/submit_new', methods = ['POST'])
def users_submit_new():
    new_user_id = User.create(request.form)
    redirect_url = '/users/' + str(new_user_id)
    return redirect(redirect_url)

@app.route ('/users/<int:id>')
def users_read(id):
    input_phrase = 'User '
    user = User.read(id)
    return render_template('user_page.html', input_phrase = input_phrase, display_read = 'static', display_update = 'none', user = user)

@app.route('/users/<int:id>/update')
def users_update(id):
    input_phrase = 'Edit user info '
    user = User.read(id)
    return render_template('user_page.html', input_phrase = input_phrase, user = user, display_read = 'none', display_update = 'static' )

# ---------------------------------------------------------------------------- #
@app.route('/submit_update', methods = ['POST'])
def users_submit_update():
    user = User.update(request.form)
    redirect_url = '/users/' + request.form['form_id']
    return redirect(redirect_url)
# ---------------------------------------------------------------------------- #
@app.route('/users/<int:id>/delete')
def users_delete(id):
    User.delete(id)
    return redirect('/users')
