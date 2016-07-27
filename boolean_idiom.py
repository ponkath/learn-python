#Boolean IDIOM

found = False
print (('Before'),found)
for value in [9,41,12,3,74,15]:
    if value == 3:
        found = True
        #add break to make code smarter, no point in printing numbers following the 3
    print (found,value)

print (('After'),found)
