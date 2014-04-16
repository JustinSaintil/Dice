#! /usr/bin/env python

import random

NumberOfDice = raw_input("How many dice")
NumberOfDice = int(NumberOfDice)

NumberOfSides = raw_input("How many sides to your dice?")
NumberOfSides = int(NumberOfSides)

dice = random.randint(1,NumberOfSides)

for Arthur in range(0,NumberOfDice):
    print "The Result is", random.randint(0,NumberOfSides)
    dice = random.randint(1,NumberOfSides)

