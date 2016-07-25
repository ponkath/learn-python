# This program says hello and asks for my name.

print('Hello world!')
print('What is your name?')   # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')   # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
print('Where do you live?')   # ask for their home
myHouse = input()
print('Wow, I always wanted to go there!')
print(myName + ', I will visit you in ' + myHouse)
