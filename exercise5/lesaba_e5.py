# Author          : John Kenneth S. Lesaba
# Course and Year : 2nd Year BS Computer Science
# Filename        : lesaba_e5.py
# Description     : driver program for exercise 5
# Honor Code      : I have not given nor received any unathorized help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.
import dice

d = dice.Dice()
print(d)
for i in range(5):
	d.roll()

d = dice.Dice(10)
print(d)
for i in range(5):
	d.roll()

d = dice.Tetrahedron()
print(d)
for i in range(10):
	d.roll()