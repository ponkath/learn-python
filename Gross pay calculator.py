#Gross pay calculator

"""
Write a program to prompt the user for hours and rate per hour using raw_input
to compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the
program (the pay should be 96.25). You should use raw_input to read a string
and float() to convert the string to a number. Do not worry about error
checking or bad user data.

hoursWorked=35
rateToday=2.75
grossPay=96.25
"""


#Python 3
print ('Enter Hours:')
hoursWorked = input()
print ('Enter Rate')
rateToday = input()
grossPay = float(hoursWorked) * float(rateToday)
print ('Your gross earning is:',grossPay)


"""
#Python 2
hoursWorked = raw_input('Enter Hours')
rateToday = raw_input('Enter Rate')
grossPay = float(hoursWorked) * float(rateToday)
print 'Your gross earning is:',grossPay
"""
