#Exercise 5.2
"""5.2 Write a program that repeatedly prompts a user for integer numbers
until the user enters 'done'. Once 'done' is entered, print out the largest
and smallest of the numbers. If the user enters anything other than a valid
number catch it with a try/except and put out an appropriate message and
ignore the number. Enter the numbers from the book for problem 5.1 and Match
the desired output as shown"""

smallest_so_far = None
largest_so_far = None
userinp = None
while True:
    userinp = raw_input('Enter a number: ')
    try:
        if userinp == 'done':
            break
        number = int(userinp)
        if smallest_so_far == None or number < smallest_so_far:
            smallest_so_far = number
        if largest_so_far == None or number > largest_so_far:
            largest_so_far = number
    except:
        print 'Invalid input'
print 'Maximum is',largest_so_far
print 'Minimum is', smallest_so_far