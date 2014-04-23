#! /usr/bin/env python

import random

NumberOfDice = raw_input("How many dice?")
NumberOfDice = int(NumberOfDice)

for x in range(0, NumberOfDice):
	NumberOfSides= raw_input("How many sides does this one have?")
	

NumberOfSides= int(NumberOfSides)
dice = random.randint(1,NumberOfSides)

for x in range(0,NumberOfDice):
    print "The Result is", random.randint(0,NumberOfSides)
    dice = random.randint(1,NumberOfSides)
