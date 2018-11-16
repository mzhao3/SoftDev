#Maggie Zhao
#SoftDev1 pd07
#K26- Getting More REST
#2018-11-15

import json #stdlib
from urllib.request import Request, urlopen #stdlib

from flask import Flask, render_template, request, session, url_for, redirect # pip install

app = Flask(__name__) #create instance of class flask



@app.route("/")
def root():

    #POKEMON TCG API
    url = "https://api.pokemontcg.io/v1/cards?subtype=Stage%201"
    u = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}))
    http = u.read()
    #print(http)
    data = json.loads(http)
    pokeData = data
    #print (data)

    #HOLIDAY API
    url = "https://holidayapi.com/v1/holidays?key=a81fb880-656a-4ee2-a182-b0148c25c7e3&country=US&year=2017&month=12"
    u = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}))
    http = u.read()
    #print(http)
    data = json.loads(http)
    holidayData = data["holidays"]
    #print(data)

    #STUDIO GHIBLI API
    url = "https://ghibliapi.herokuapp.com/vehicles"
    u = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}))
    http = u.read()
    #print(http)
    data = json.loads(http)
    ghibliData = data
    print(data)


    return render_template("index.html", poke = pokeData["cards"][8], holiday = holidayData, ghibli = ghibliData)



if __name__ == "__main__":
    app.debug = True
    app.run()
