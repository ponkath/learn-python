#Score2 - Excercise 4.7 COMPUTEGRADE

"""
score = input('Enter score: ')
scr = float(score)

if float(score) >0 and float(score) <=1:
        if float(score) < 0.6:
                print ('F')
        elif float(score) <= 0.7:
                print ('D')
        elif float(score) <= 0.8:
                print ('C')
        elif float(score) <= 0.9:
                print ('B')
        elif float(score) <= 1.0:
                print ('A')
else:
	print ('Bad score!')
"""

def computegrade(score):
    if float(score) >0 and float(score) <=1:
            if float(score) < 0.6:
                    score = ('F')
            elif float(score) <= 0.7:
                    score = ('D')
            elif float(score) <= 0.8:
                    score = ('C')
            elif float(score) <= 0.9:
                    score = ('B')
            elif float(score) <= 1.0:
                    score = ('A')
    else:
            print ('Bad score!')

score = input('Enter score: ')
scr = float(score)

print ('Your score is: ' + str(computegrade(score)))
