# simon- Maggie Zhao, Amit Narang
# SoftDev1 pd7
# K10: Jinja Tuning
# 2018-09-22

#============================================================================
from flask import Flask, render_template
from random import random, choices

app = Flask(__name__)

#============================================================================
def makeOccupationDict():
	new_dict = {}

	f = open("occupations.csv", "r") # Opens file for reading

	for line in f.readlines(): # f.readlines() returns a list of lines

		line = line.replace('"', "") # Removes the unnecessary extra quotes

		line = line.strip() # Removes all extra new lines
		occupation_percentage = line.rsplit(",", 1) # Splits line in the format ["OCCUPATION", "PERCENTAGE"]

		if occupation_percentage[0] in "Job Class Total": # If the 1st value of the line is "Job Class" or "Total" skip it
			continue

		new_dict[occupation_percentage[0]] = float(occupation_percentage[1])
		# Creates a new value in the form {"OCCUPATION": PERCENTAGE}

	f.close()

	return new_dict

#creates a new dictionary using the occupation.csv
occupation_dict = makeOccupationDict()

#============================================================================
def weightedAverageOccupation(dictOfOccupations):
	#creates list of occupations
    listOcc = list(dictOfOccupations.keys())

	#creates list of percentages of how common the occupation is (which is the weight for randomization)
    listWeight = list(dictOfOccupations.values())

	#choices(population, weights=None, *, cum_weights=None, k=1) is imported from random
    #Return a k sized list of elements chosen from the population with replacement. If the population is empty, raises IndexError.
    return "" + choices(listOcc,listWeight)[0]

#============================================================================
#route to occupations page
@app.route('/occupations')
def occupations():
	#renders occupations.html
	#choice is the occupation chosen randomly
	#parent_dict is the dictionary of occupations
    return render_template('occupations.html', choice = weightedAverageOccupation(occupation_dict), parent_dict = occupation_dict)

#============================================================================
#runs the app
if __name__ == "__main__":
    app.debug = True
    app.run()
