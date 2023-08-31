from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return'hello, world'

@app.route('/dojo')
def text_dojo():
    return 'dojo'

@app.route('/say/<string:name>')
def say_name(name):
    print (name)
    return 'hi ' + name + '!'

@app.route('/repeat/<int:number>/<string:string>')
def repeat_number(number, string):
    return (string + " ") * number

if __name__=='__main__':
    app.run(debug = True)