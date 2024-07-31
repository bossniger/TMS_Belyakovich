from flask import Flask, request, render_template
import requests

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def square_number():
    if request.method == 'POST':
        number = int(request.form['number'])
        square = number * number
        return render_template('index.html', number=number, square=square)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
