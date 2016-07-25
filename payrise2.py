#payrise2
"""Rewrite your pay computation to give the employee 1.5 times the hourly rate
for hours worked above 40 hours.

Enter Hours: 20
Enter Rate: 9
Pay 475.0

Use try/except to print out a message to user for
non numeric input

45*10=450
5*(10*1.5)=75
TOTAL=475
"""
hours = input('Enter hours: ')
try:
	h = float(hours)
	rate = input('Enter Rate: ')
	r = float(rate)
except:
	print ('Please enter a number.')

if float(hours) <= 40:
	pay = (h * r)
else:
	pay = ((r * 40)+((r * 1.5)*(h - 40)))
print ('Your earned',pay,'for',hours,'hours of work.')
