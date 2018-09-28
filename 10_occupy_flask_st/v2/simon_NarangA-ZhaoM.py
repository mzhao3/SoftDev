# simon - Maggie Zhao, Amit Narang
# SoftDev1 pd7
# K10: Jinja Tuning
# 2018-09-22
import util.app as app1
from flask import Flask, render_template

app = Flask(__name__)
occupation_dict = app1.makeOccupationDict("data/occupations.csv")

@app.route('/occupations')

def occupations():
    return render_template('occupations.html', randomAtTop = app1.weightedAverageOccupation(occupation_dict), parent_dict = occupation_dict)

if __name__ == "__main__":
    app.debug = True
    app.run()
