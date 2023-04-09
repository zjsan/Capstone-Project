from flask import Flask, render_template, url_for
import test

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
@app.route('/index/#selectroom/')
@app.route('/index/#aboutus/')
def index():
    return render_template('index.html')


@app.route('/index/#selectroom/')
def show_data():


if __name__ == '__main__':
    app.run(debug=True)