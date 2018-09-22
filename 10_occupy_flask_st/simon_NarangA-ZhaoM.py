from flask import Flask, render_template
from random import random, choices

app = Flask(__name__)
def makeOccupationDict():
	new_dict = {}

	f = open("occupations.csv", "r") # Opens file for reading

	for line in f.readlines(): # f.readlines() returns a list of lines

		line = line.replace('"', "") # Removes the unnecessary extra quotes

		line = line.strip() # Removes all extra new lines
		occupation_percentage = line.rsplit(",", 1) # Splits line in the format ["OCCUPATION", "PERCENTAGE"]

		if occupation_percentage[0] in "Job Class Total": # If the 1st value of the line is "Job Class" or "Total" skip it
			continue

		new_dict[occupation_percentage[0]] = float(occupation_percentage[1])/100 # Creates a new value in the form {"OCCUPATION": PERCENTAGE}

		#print(new_dict.keys(), new_dict[occupation_percentage[0]], new_dict.values())

	f.close()

	return new_dict
'''
def convertDictToHTML(diction):
    #s = "<table style = \"width:100%\">"
    s += '\n'
    for i in diction:
        s += '<tr>'
        s += '\n'
        s += '<td>'
        s += i
        s += '</td>'
        s += '\n'
        s += '<td>'
        s += str(diction.get(i))
        s += '</td>'
        s += '\n'
        s += '</tr>'
        s += '\n'
    #s += '</table>'
    return s
'''
def weightedAverageOccupation(dictOfOccupations):
    listOcc = list(dictOfOccupations.keys())
    listWeight = list(dictOfOccupations.values())
    return "" + choices(listOcc,listWeight)[0]

occupation_dict = makeOccupationDict()
rando = weightedAverageOccupation(occupation_dict)

@app.route('/occupations')

def occupations():
    return render_template('occupations.html', randomAtTop = rando, parent_dict = occupation_dict)

if __name__ == "__main__":
    app.debug = True
    app.run()
