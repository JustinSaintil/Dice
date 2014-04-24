#! /usr/bin/env python

import random

NumberOfDice = raw_input("How many dice?")
NumberOfDice = int(NumberOfDice)

for x in range(0, NumberOfDice):
	NumberOfSides= raw_input("How many sides does this one have: ")
	NumberOfSides= int(NumberOfSides)
	while NumberOfSides <= 1:
		NumberOfSides= raw_input("Please input a number that is larger than one: ")
		NumberOfSides= int(NumberOfSides)
	print "The Result is", random.randint(1,NumberOfSides)
	dice = random.randint(1,NumberOfSides)

		 




