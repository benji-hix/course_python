from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html', phrase = 'hello', times = 5)

@app.route('/list')
def render_list():
    persons = [
        {'name' : 'benji', 'soup' : 'mushroom'},
        {'name' : 'liz', 'soup': 'french onion'},
        {'name' : 'judith', 'soup' : 'zuppa toscana'}
    ]
    return render_template('index.html', persons = persons)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
