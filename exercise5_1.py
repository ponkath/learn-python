#Exercise 5.1
"""Write a program which repeatedly reads numbers until the user enters
“done”. Once “done” is entered, print out the total, count, and average of
the numbers. If the user enters anything other than a number, detect their mistake
using try and except and print an error message and skip to the next number."""

userint = input('Enter a number: ')
while userint:
    if userint == 'done':
        print ('done')
        break
    else:
        try:
            u = float(userint)
            
        except:
            print ('bad data')
print (total,count,avarage)

