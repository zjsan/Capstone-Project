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
def get_data():

    #checking the form user submitted
    #validating forms
    selected = ""

    if request.method == "GET":

        if request.args['submit'] == 'submit_office':
            office = request.args['offices']
            selected = office
            return selected
        if request.args['submit'] == 'submit_lab':
            lab = request.args['labrooms']
            return lab
        if request.args['submit'] == 'submit_lecture':
            lecture_room = request.args['lecturerooms']
            return lecture_room
    else:
        return redirect('index.html/#selectroom')

@app.route("/<room>")
def show_data(room):
    return f"<h1>{room}</h1>"

if __name__ == '__main__':
    app.run(debug=True)