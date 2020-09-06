# Author          : John Kenneth S. Lesaba
# Course and Year : 2-BS Computer Science
# Filename        : lesaba_e2.py
# Description     : Graded Lab Exercise 2: Python Data Structures
# Honor Code      : I have not given nor received any unathorized help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.

data = {"Complete Name": "John Kenneth S. Lesaba",
        "Spirit Animal": "Sloth",  
        "Reason": "oftentimes I'm lazy",
        "Hobbies": ["Watch YouTube or Netflix", "Play online games", "Drive"],
        "Profession": "Software Engineer"}

print("I am ", data["Complete Name"], ".", sep="")
print("My spirit animal is ", data["Spirit Animal"], ",", sep="")
print("because ", data["Reason"], ".", sep="")
print("When not in school, I love to:",
    "\n*", data["Hobbies"][0],
    "\n*", data["Hobbies"][1],
    "\n*", data["Hobbies"][2])
print("I dream of being a", data["Profession"], "in the future.")