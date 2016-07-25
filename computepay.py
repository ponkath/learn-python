#computepay excercise

"""
time-and-half for <40h work

Enter Hours: 45
Enter Rate: 10
Pay: 475.0

using a function:
def computepay


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
"""

"""
def computepay(h,r):
    return 42.37

hrs = raw_input("Enter Hours:")
p = computepay(10,20)
print "Pay",p
"""
# take input and put into function eg. computepay('43')

#h = input.computepay('43')
##########################################################

    
def computepay(h,r):
        if float(hours) <= 40:
            pay = (h * r)
        else:
            pay = ((r * 40)+((r * 1.5)*(h - 40)))
        return pay

try:
        hours = input('Enter hours: ')
        h = float(hours)
        rate = input('Enter Rate: ')
        r = float(rate)
except:
        print ('Please enter a number.')
print ('Your earned',computepay(h,r),'for',hours,'hours of work.')


