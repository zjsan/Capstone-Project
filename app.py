from flask import Flask, render_template, url_for, request, redirect
import test

app = Flask(__name__)


#defining view routes
@app.route('/')
@app.route('/index/')
@app.route('/index/#selectroom/')
@app.route('/index/#aboutus/')
def index():
    return render_template('index.html')


@app.route('/#selectroom/', methods = ["GET","POST"])
def send_data():

    #trying out flask html form data retrieval
    if request.method == "GET":
         selected = request.args['offices']
         return selected
    else:
        return redirect('index.html/#selectroom')

@app.route("/<room>")
def show_data(room):
    return f"<h1>{room}</h1>"

if __name__ == '__main__':
    app.run(debug=True)