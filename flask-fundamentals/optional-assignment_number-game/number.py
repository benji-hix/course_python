from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'yoshi yoshi yoshi yoshi yoshi'

@app.route('/')
def index():
    if 'correct_number' in session:
        pass
    else:
        session['correct_number'] = random.randint(1, 100)
    return render_template('number.html', display_incorrect = 'none', display_correct = 'none')

@app.route('/destroysession')
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/guess', methods=['POST'])
def guess():
    current_guess = int(request.form['user-guess'])
    if current_guess < session['correct_number']:
        return redirect('/too-low')
    elif current_guess > session['correct_number']:
        return redirect('/too-high')
    else:
        return redirect('/correct')

@app.route('/too-high')
def guess_too_high():
    session['phrase'] = 'Guess is too high. Please guess again.'
    print("redirected to too-high")
    return render_template('number.html', display_incorrect = 'static', display_correct = 'none')

@app.route('/too-low')
def guess_too_low():
    session['phrase'] = 'Guess is too low. Please guess again.'
    print("redirected to too-low")
    return render_template('number.html', display_incorrect = 'static', display_correct = 'none')


@app.route('/correct')
def guess_correct():
    print("redirected to correct")
    session['phrase'] = ' was the correct number.'
    return render_template('number.html', display_incorrect = 'none', display_correct = 'static')


if __name__=='__main__':
    app.run(debug=True)