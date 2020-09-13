# Author          : John Kenneth S. Lesaba
# Course and Year : 2-BS Computer Science
# Filename        : lesaba-proba.py
# Description     : A program that prints a triangle shape composed of specific ASCII character.
# Honor Code      : I have not given nor received any unathorized help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.
T = int(input())                            # user input `T` test cases
for x in range(T):                          # loops according to the number of test cases `T`
    (k, c) = input().split()                # input of `k` which pertains to triangle's height and `c` which is the ascii character that will form the triangle
    k = int(k)                              # sets variable k as integer

    print("CASE ", x + 1, ":", sep="")      #prints a line containing the word CASE followed by a single space, the case number starting from 1, and a colon (:).
    row = 1                                 #sets the start of row as 1
    while row <= k:                         #while loop as the number of rows increase to the height `k`
        for col in range(k-row):            #for loop to compute the number of columns where whitespace is printed
            print(end=" ")                  #prints whitespace
        if row == 1:                        #if statement for the first row
            print(c,end="")                 #prints one instance of `c`
        else:                               #else statement for succeeding rows
            for col in range(row*2-1):      #for loop to compute the number of colums where `c` is printed
                print(c,end="")             #prints `c`
        print()                             #prints a nextline (`\n`) character
        row = row + 1                       #increments row by 1