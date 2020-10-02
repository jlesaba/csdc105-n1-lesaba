# Author          : John Kenneth Seva Lesaba
# Course and Year : BS Computer Science - 2nd year
# Filename        : lesaba_e4.py
# Description     : driver file for Graded Exercise #4
# Honor Code      : I have not given nor received any unathorized help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.
import geometry as g
(a,b,c) = input("Enter the side lengths of a triangle: ").split(sep=",")
if(g.check_lenghts(float(a),float(b),float(c))):
    print("Perimeter: {:.2f}".format(g.perimeter(float(a),float(b),float(c))))
    print("Area: {:.2f}".format(g.triangle_heronsarea(float(a),float(b),float(c))))
else:
    print("Error: Invalid input")