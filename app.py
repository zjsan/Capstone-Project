from flask import Flask, render_template, url_for, request, redirect
from test import *

app = Flask(__name__)


#defining view routes
@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/index/#roomselect')
def room():
    return redirect('/index/#roomselect')

@app.route('/path/', methods = ["GET","POST"])
def get_data():

    #checking the form user submitted
    #validating formsX
    selected = ""
    direction = []

    if request.method == "GET":

        #passing arguments to the AI based on the selected input
        if request.args['submit'] == 'submit_office':
            office = request.args['offices']
            selected = office
            direction =  main_ai(selected)#passing user input to the ai

            #returning the generated path/direction to the web browser
            return render_template('direction.html',direction = direction)
        
        if request.args['submit'] == 'submit_lab':
            lab = request.args['labrooms']
            selected = lab
            direction = main_ai(selected)#passing user input to the ai
          
            #returning the generate path/direction to the web server
            return render_template('direction.html',direction = direction)
        if request.args['submit'] == 'submit_lecture':
            lecture_room = request.args['lecturerooms'] 
            selected = lecture_room
            direction = main_ai(selected)#passing user input to the ai

            #returning the generate path/direction to the web server
            return render_template('direction.html',direction = direction)
    #fall back mechanism
    else:
        return redirect(url_for('index.html'))

#@app.route("/<room>")
#def show_data(room):
   # return f"<h1>{room}</h1>"

if __name__ == '__main__':
    app.run(debug=True)