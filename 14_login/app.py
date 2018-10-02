# Maggie Zhao & Jiajie Mai & Alexander Liu
# SoftDev1 pd7
# K14-- Do I Know You?
# 2018-10-02
from flask import Flask, render_template, request, session, url_for, redirect

import os

app = Flask(__name__)

app.secret_key = os.urandom(32)

userDict = {'alex' : 'starwars4'}

@app.route('/', methods = ["GET", "POST"] )
def disp_login():
    if 'username' in session:
        return render_template("welcome.html", username = session['username'])
    else:
        loginMess = "Please enter a valid username and password."
        return redirect('/auth')

@app.route('/auth', methods = ["GET", "POST"] )
def authenticate():
    if request.method == "GET":
        # if logged in
        if 'username' in session:
            return render_template("welcome.html", username = session['username'])
        # if not logged in
        else:
            loginMess = "Please enter a valid username and password."
            return render_template("login.html", message = loginMess)

    username = request.form['username']
    password = request.form['password']

    ### Invalid username: ===================================
    if username not in userDict.keys():
        errorMess = "*cue sad trombone music* It looks like you've entered an invalid username. Please try again."
        #print('bad username')
        return (render_template("login.html", message = errorMess))

    ### Invalid password: ===================================
    elif userDict['alex'] != password:
        errorMess = "*cue sad trombone music* It looks like your password does not match your username. Please try again."
        print('bad password')
        return  (render_template("login.html", message = errorMess))

    ### Both username and password are valid ================
    elif username in userDict.keys() and userDict['alex'] == password:
        session['username'] = username
        return redirect("/")

    ### All other invalid cases =============================
    else:
        errorMess = "Oops! Looks like something went wrong. Please try again."
        return ( (render_template("login.html", message = errorMess )))

@app.route('/logout')
def logout():
    session.pop('username')
    #return ( render_template ( "login.html", message = "You have been successfully logged out."))
    return redirect(url_for("authenticate"))
if __name__ == "__main__":
    app.debug = True
    app.run()
