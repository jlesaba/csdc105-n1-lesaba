# Author          : John Kenneth S. Lesaba
# Course and Year : 2nd Year BS Computer Science
# Filename        : dice.py
# Description     : dice module for exercise 5
# Honor Code      : I have not given nor received any unathorized help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.
from random import randint
class Dice:
	def __init__(self, sides = 6):
		self.sides = sides
	
	def roll(self):
		print(randint(1, self.sides))
		
	def __str__(self):
		return "DICE: {}".format(self.sides)

class Tetrahedron(Dice):
    def __init__(self):
        super().__init__(4)