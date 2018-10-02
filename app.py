from flask import Flask, render_template, request, flash
import os
app = Flask(__name__)

app.secret_key = os.urandom(32)

@app.route('/')
def hello_world():
    print(app)
    flash ("hello!")
    return render_template("jinja_template.html")

@app.route('/auth')
def authenticate():
    '''
    print(app)
    print(request) ##prints returned URL with auth tags
    print(request.args) ## gives immutabledict based on names of input fields (ie username & sub1)
    print(request.args['username'])
    print(request.headers)
        #print (url_for('disp_login'))
        #print (url_for('authenticate'))
        #return redirect(url_for("disp_login"))
    return "Waaaa hooo HAAAH"
    '''

if __name__ == "__main__":
    app.debug = True
    app.run()
