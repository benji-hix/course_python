from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models import survey

@app.route('/survey')
def index():
    return render_template('survey.html')

@app.route('/submit', methods=['POST'])
def submit_survey():
    if not survey.Survey.validate_survey(request.form):
        return redirect('/survey')
    
    survey.Survey.create(request.form)
    survey_data = survey.Survey.read_all()
    return render_template('/result.html', survey_data=survey_data)