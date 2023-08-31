from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('checkerboard_index.html')

@app.route('/<int:rows>/<int:columns>/<string:color_1>/<string:color_2>')
def generate_board(rows, columns, color_1, color_2):
    return render_template('checkerboard_index.html', rows = rows, columns = columns, color_1 = color_1, color_2 = color_2)

if __name__ == '__main__':
    app.run(debug = True)