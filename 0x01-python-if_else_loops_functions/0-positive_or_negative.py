#!/usr/bin/python3
import random
number = random.randint(-10, 10)

#My code
if number > 0:
	print("{} is positive".format(number))
else:
	if number < 0:
		print("{} is negative".format(number))

