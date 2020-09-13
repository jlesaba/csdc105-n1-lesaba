# Author          : John Kenneth S. Lesaba
# Course and Year : 2-BS Computer Science
# Filename        : lesaba-probb.py
# Description     : A program that reads a string in `X.X.X.X` format and determine if the string is a valid IPv4 address in the dotted decimal format.
# Honor Code      : I have not given nor received any unathorized help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.
T = int(input())                                                #input `T` number of cases
for x in range(T):                                              #loop to repeat `T` times
    string = [s for s in input().split(".")]                    #input list string by separating input via the dot(.) character as separator
    valid = False                                               #initialize boolean `valid` to false. This will be used to store result in checking each element of the list
    if(len(string) == 4):                                       #if list contains 4 elements then proceed, if not print validity as invalid
        for i in range(4):                                      #loop to access each element of the list with `i` as index
            if int(string[i]) >= 0 and int(string[i]) <= 255:   #if statement in checking the validity of each element of string
                valid = True                                    #set `valid` as true if the condition above is true
            else:                                               #else statement if above if statement is false
                valid = False                                   #set `valid` as false
                break                                           #break from loop as one element of the list invalid renders the entire list as invalid
    print("CASE ", x+1, ":", sep="", end=" ")                   #prints the word CASE followed by a single space, the case number starting from 1, a colon (:), and a single space.
    if(valid):                                                  #if the boolean `valid` is True
        print("VALID")                                          #print the word VALID
    else:                                                       #if the boolean `valid` is False
        print("INVALID")                                        #print the word INVALID
