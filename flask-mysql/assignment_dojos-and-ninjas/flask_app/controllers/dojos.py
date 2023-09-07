from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/dojos')
def index():
    all_dojos = Dojo.get_all()
    return render_template('home.html', all_dojos = all_dojos)

@app.route('/dojos/<int:dojo_id>')
def show_dojo(dojo_id):
    dojo = Dojo.read(dojo_id)
    dojo_ninjas = Ninja.read_ninjas(dojo_id)
    return render_template('dojos.html', dojo_ninjas = dojo_ninjas, dojo=dojo)

@app.route('/submit_dojo', methods = ['POST'])
def submit_new_dojo():
    Dojo.create(request.form)
    return redirect('/dojos')