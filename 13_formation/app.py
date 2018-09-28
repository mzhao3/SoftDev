# Maggie Zhao
# SoftDev1 pd7
# K13
# 2018-09-27


from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    ##print(app)
    return render_template("form.html")

@app.route('/auth')
def authenticate():
    ## returns value of 'username' from the immutabledict, which is based on names of input fields
    username =  request.args['username']

    ## returns the method used was GET or POST
    ##  GET: retrieves information from the server
    ##  POST: requests that a web server accepts the data enclosed in the body of the request message, most likely for storing it.
    method = request.method
    greeting = "Hello <b>" + username + "</b>! I'm Rick Harrison, and this is my pawn shop. I work here with my old man and my son, Big Hoss. Everything in here has a story and a price. One thing I've learned after 21 years - you never know what is gonna come through that door."
    
    returnStr = "<b>Username: </b> " + username + "<br>" + "Method: <b> "+ method +"</b><br>"+greeting

    return returnStr

if __name__ == "__main__":
    app.debug = True
    app.run()
