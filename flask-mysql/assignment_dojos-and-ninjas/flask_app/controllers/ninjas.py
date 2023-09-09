from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def new_ninja():
    all_dojos = Dojo.get_all()
    return render_template('ninjas.html', all_dojos = all_dojos)

@app.route('/submit_ninjas', methods = ['post'])
def submit_new_ninja():
    Ninja.create(request.form)
    redirect_url = '/dojos/' + request.form['form_dojo_id']
    return redirect(redirect_url)
