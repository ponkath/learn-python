#Score - Excercise 3.3

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
