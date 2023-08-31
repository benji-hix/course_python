from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('playground_index.html', box_number = 3)

@app.route('/play/<int:box_number>')
def multiple_boxes(box_number):
    return render_template('playground_index.html', box_number = box_number) 

@app.route('/play/<int:box_number>/<string:box_color>')
def colored_boxes(box_number, box_color):
    return render_template('playground_index.html', box_number = box_number, box_color = box_color)

if __name__ =='__main__':
    app.run(debug = True)