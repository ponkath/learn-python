#greet function example

def greet(lang):
	if lang == 'es':
		print ('Hola')
	elif lang == 'fr':
		print ('Salut')
	elif lang == 'de':
		print ('Hallo')
	else:
		print ('Hello')

"""
Output

>>>greet('en')
Hello
>>>greet('es')
Hola

QUESTION: how to call multiple lang?
"""
