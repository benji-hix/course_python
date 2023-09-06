from flask import render_template, Flask, request, redirect
from user import User

app = Flask(__name__)

@app.route('/users')
def index():

    all_users = User.get_all()
    return render_template('read.html', all_users = all_users)

@app.route('/users/new')
def users_create():
    return render_template('create.html')

@app.route('/submit', methods = ['POST'])
def users_new():
    User.create(request.form)
    return redirect('/users')

if __name__ == '__main__':
    app.run(debug=True)
