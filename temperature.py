#Temperature: Celsius to Fahrenheit converter

"""How to convert Celsius to Fahrenheit
The temperature T in degrees Fahrenheit (°F) is equal to the temperature T in degrees Celsius (°C) times 9/5 plus 32:
T(°F) = T(°C) × 9/5 + 32
or
T(°F) = T(°C) × 1.8 + 32
"""

cel = input('Enter Celsius: ')
fah = (float(cel)) * 1.8 + 32.0
print (fah)
