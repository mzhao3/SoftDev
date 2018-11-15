#Maggie Zhao
#SoftDev1 pd07
#K24- Getting more REST
#2018-11-14

import json #stdlib
import urllib.request #stdlib

from flask import Flask, render_template, request, session, url_for, redirect # pip install


#KEY_FBI = "DEMO_KEY"
KEY_FBI = "hqief9VhqpfYTbii2HQjh8TlmoVyVRKf0wrFvbFj"
URL_STUB = "https://api.usa.gov/crime/fbi/sapi"
ENDPOINT = "/api/data/nibrs/larceny/offender/national/age"
URL = URL_STUB + ENDPOINT + "?api_key="+ KEY_FBI

app = Flask(__name__) #create instance of class flask

# retrieves appropriate API

@app.route("/")
def root():

    #print(URL)

    # opens url, which can be either a string or a request object
    # returns a bytesobject
    u = urllib.request.urlopen(URL)

    # pulls data from the network
    # returns all the bytes of the object
    http = u.read()

    #print(http)

    # takes string and returns a dictionary
    data = json.loads(http) #save JSON obj
    #print (data)

    # renders template with table of info from API
    return render_template("index.html", data = data['results'])


if __name__ == "__main__":
    app.debug = True
    app.run()
