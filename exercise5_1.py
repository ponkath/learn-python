#Exercise 5.1
"""Write a program which repeatedly reads numbers until the user enters
“done”. Once “done” is entered, print out the total, count, and average of
the numbers. If the user enters anything other than a number, detect their mistake
using try and except and print an error message and skip to the next number."""

counter = 0
total = 0
average = 0
userinp = None
while True:
    userinp = input('Enter a number: ')
    try:
        if userinp == 'done':
            break
        number = int(userinp)
        counter = counter + 1
        total = total + number
    except:
        print ('bad data')
if counter > 0:
    average = total / counter
print (total,counter,average)
