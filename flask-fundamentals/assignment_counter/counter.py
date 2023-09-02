from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'oh the misery'

@app.route('/')
def index():
    if ('true_count' in session):
        session['true_count'] +=1
        print("true count:", session['true_count'])
    else:
        session['true_count'] = 1
        print("true count:", session['true_count'])

    if ('count' in session):
        session['count'] += 1
        print("viewer count:", session['count'])
    else:
        session['count'] = 1
        print("viewer count:", session['count'])
    return render_template('counter.html')

@app.route('/click', methods=['POST'])
def button_click():
    if (request.form.get('count-up') == 'count-up-1'):
        return redirect('/')
    elif (request.form.get('reset') == 'reset-1'):
        session.pop('count')
        return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)