from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'it\'s the secret key for me, sis'

@app.route('/')
def index():
    return render_template('survey.html')

@app.route('/submit', methods=['POST'])
def submit_survey():
    session['name'] = request.form['input-name']
    session['location'] = request.form['input-location']
    session['language'] = request.form['input-language']
    session['comment'] = request.form['input-comment']
    return render_template('/result.html')

@app.route('/return', methods=['POST'])
def return_to_survey():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)