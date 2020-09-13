# Author          : John Kenneth S. Lesaba
# Course and Year : 2-BS Computer Science
# Filename        : lesaba-probb.py
# Description     : A program that reads an integer and prints the sequence of Fibonacci numbers as a comma-separated list on a single line.
# Honor Code      : I have not given nor received any unathorized help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.
T = int(input())                                #input `T` number of test cases
for x in range(T):                              #loop to repeat `T` times
    n = int(input())                            #input integer `n`
    a = 0                                       #initialize F_0 as integer variable `a` equals zero
    b = 1                                       #initialize F_1 as integer variable `b` equals 1
    count = 0                                   #initialize counter to zero
    print("CASE ", x + 1, ": ", sep="", end="")         #print the word CASE followed by a single space, the case number starting from 1, a colon (:), and a single space.

    if n >= 0:                                  #Constraint n is greater than or equal to zero
        while count <= n:                       #while loop to repeat computation and printing of Fibonacci sequence until it reaches F_N
            if count < n:                       #if condition when count is not yet equal to n
                print(a, end=",")              #if the above is true, then print the F_a followed by a comma
            else:                               #when count is equal to n
                print(a)                        #output F_n then go to next line
            temp = a + b                        #temporary variable that holds the next number in the sequence
            a = b                               #assigns a = b as b holds the next number to be printed
            b = temp                            #assigns the next number in the sequence (temp) to b
            count = count + 1                   #increments the counter by 1
        
