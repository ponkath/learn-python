#Exercise 5.2
"""Write a program which repeatedly reads numbers until the user enters
“done”. Once “done” is entered, print out the total, count,  minimum and maximum of
the numbers. If the user enters anything other than a number, detect their mistake
using try and except and print an error message and skip to the next number."""

#TODO: create function, write tests, backwards compatible/version agnostic
    
counter = 0
total = 0
smallest_so_far = None
largest_so_far = None
userinp = None
while True:
    userinp = input('Enter a number: ')
    try:
        if userinp == 'done':
            break
        number = int(userinp)
        counter = counter + 1
        total = total + number
        if smallest_so_far == None or number < smallest_so_far:
            smallest_so_far = number
        if largest_so_far == None or number > largest_so_far:
            largest_so_far = number
    except:
        print ('bad data')
print (total,counter,smallest_so_far,largest_so_far)
