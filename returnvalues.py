#Return values

def greet():
	return "Hello"

print greet(), "Kathleen"
print greet(), "Luciano"

"""
returns

Hello Kathleen
Hello Luciano
"""

#greet function example

def greet(lang):
	if lang == 'es':
		return ('Hola')
	elif lang == 'fr':
		return ('Salut')
	elif lang == 'de':
		return ('Hallo')
	else:
		return ('Hello')

"""
>>>print greet('de'),'Kathleen'
Hallo Kathleen
>>>print greet('es'),'Luciano'
Hola Luciano
"""

"""
fruitful: produce values
void: others
"""