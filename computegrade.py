#Score2 - Excercise 4.7 COMPUTEGRADE

'''Exercise 4.7 Rewrite the grade program from the previous chapter using a function
called computegrade that takes a score as its parameter and returns a grade
as a string.'''

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

def computegrade(score_input):

    grade = 'Bad score!'
    
    try:
        score = float(score_input)
    except:
        score = -1

    if score >0 and score <=1:
            if score < 0.6:
                    grade = ('F')
            elif score <= 0.7:
                    grade = ('D')
            elif score <= 0.8:
                    grade = ('C')
            elif score <= 0.9:
                    grade = ('B')
            elif score <= 1.0:
                    grade = ('A')
    return grade


score_str = input('Enter score: ')
print ('Your score is: ' + computegrade(score_str))
