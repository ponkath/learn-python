#payrise
"""Rewrite your pay computation to give the employee 1.5 times the hourly rate
for hours worked above 40 hours.

Enter Hours: 45
Enter Rate: 10
Pay 475.0

45*10=450
5*(10*1.5)=75
TOTAL=475
"""
hours = input('Enter hours: ')
h = float(hours)
rate = input('Enter Rate: ')
r = float(rate)

if float(hours) <= 40:
	pay = (h * r)
else:
	pay = ((r * 40)+((r * 1.5)*(h - 40)))
print ('Your earned',pay,'for',hours,'hours of work.')
