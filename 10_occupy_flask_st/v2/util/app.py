
from random import random, choices

def makeOccupationDict(s):
	new_dict = {}

	f = open(s, "r") # Opens file for reading

	for line in f.readlines(): # f.readlines() returns a list of lines

		line = line.replace('"', "") # Removes the unnecessary extra quotes

		line = line.strip() # Removes all extra new lines
		occupation_percentage = line.rsplit(",", 1) # Splits line in the format ["OCCUPATION", "PERCENTAGE"]

		if occupation_percentage[0] in "Job Class Total": # If the 1st value of the line is "Job Class" or "Total" skip it
			continue

		new_dict[occupation_percentage[0]] = float(occupation_percentage[1]) # Creates a new value in the form {"OCCUPATION": PERCENTAGE}

		#print(new_dict.keys(), new_dict[occupation_percentage[0]], new_dict.values())

	f.close()

	return new_dict

def weightedAverageOccupation(dictOfOccupations):
    listOcc = list(dictOfOccupations.keys())
    listWeight = list(dictOfOccupations.values())
    return "" + choices(listOcc,listWeight)[0]
