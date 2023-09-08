from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import email

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods = ['POST'])
def submit_email():
    if not email.Email.validate_email(request.form):
        return redirect('/')
    email.Email.create(request.form)
    session['email'] = request.form['form_email']
    return redirect('/all_emails')

@app.route('/all_emails')
def all_emails():
    all_emails = email.Email.read_all()
    return render_template('table.html', all_emails=all_emails)
    
@app.route('/delete/<int:pk>')
def delete(pk):
    email.Email.delete(pk)
    return redirect('/all_emails')
