# Author          : John Kenneth Seva Lesaba
# Course and Year : BS Computer Science - 2nd year
# Filename        : geometry.py
# Description     : geometry module for lesaba_e4.py
# Honor Code      : I have not given nor received any unathorized help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.
from math import sqrt
def perimeter (*side_lengths):
    perimeter = 0
    for s in side_lengths:
        perimeter += s
    return round(perimeter,2)

def triangle_heronsarea (a, b, c):
    s = perimeter(a,b,c) / 2
    result = s * (s - a) * (s - b) * (s - c)
    return round(sqrt(result),2)

def check_lenghts(*side_lengths):
    for s in side_lengths:
        if s <= 0:
            return False
    side_lengths = sorted(side_lengths)
    if side_lengths[0] + side_lengths[1] > side_lengths[2]:
        return True
    else:
        return False