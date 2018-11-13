#Maggie Zhao
#SoftDev1 pd07
#K24- A RESTful Journey Skyward
#2018-11-13

from flask import Flask, render_template, request, session, url_for, redirect

import json
# module defines functions and classes which help in opening URLS (mostly HTTP)
import urllib.request

app = Flask(__name__) #create instance of class flask

# retrieves appropriate API
url = "https://api.nasa.gov/planetary/apod?api_key=Atai4hAKS9ngaHHMLqqIQncUqXs1OzYxwe65qwsh&date=2017-02-02"

@app.route("/")
def root():
    # opens url, which can be either a string or a request object
    # returns a bytesobject
    u = urllib.request.urlopen(url)

    # pulls data from the network
    # returns all the bytes of the object
    http = u.read()

    #print(http)

    # takes string and returns a dictionary
    data = json.loads(http)
    #print (data)

    # renders template with displayed image from API call & has explanation
    return render_template("index.html", pic = data['url'], explanation = data['explanation'])


if __name__ == "__main__":
    app.debug = True
    app.run()
