"""
Name: Gloria Pappalardo
Date created: September 11, 2020
Lab 2
In the first part of this lab, I created a function that takes the input of a temperature and outputs a printed summary
of how hot, warm, cool, or cold it is based on ranges of temperatures in Fahrenheit. In the second part of the lab, I
created a chatbot that communicates with the user by name. The chatbot asks for two numerical inputs, and for the first
one returns the square of the number, and for the second returns the square root.
"""

# first part of lab
# input prompt, then convert str to int
temp = int(input('What is the temperature today?'))
# temperature given in Fahrenheit (F) for function
def feelTemp(temp):
# if temperature is above 100 F, prints 'It is hot.'
  if temp >= 100:
    print('It is hot.')
# if temperature is at least 70 and less than 100 F, prints 'It is warm.'
  elif temp >= 70 and temp < 100:
    print('It is warm.')
# if temperature is at least 32 and less than 70 F, prints 'It is cool.'
  elif temp < 70 and temp >= 32:
    print('It is cool.')
# in all other cases, whereby temperature is under 32 F, prints 'It is cold.'
  else:
    print('It is cold.')

feelTemp(temp)

# second part of lab
import math
# prompt name input from user
name_prompt = input('Hi, I\'m a chatbot named El. What\'s your name?')
# print response, a personalized greeting
if name_prompt == 'El':
    print('Wow! We have the same name. Hello, El.')
else:
    print('Hello', name_prompt, '!')
# prompt user for a number, which will be squared
prompt_exp = input('I can do math. Tell me a whole number.')
# perform exponentiation on the number
square = int(prompt_exp) ** 2
# print the square of the number to user
print('Thank you,', name_prompt, '. The square of your number is', square, '.')
# second number prompt, which will return the square root of the number
prompt_root = input(' I\'m a regular mathematical machine. What\'s another number you like?')
# perform square root on number
square_root = math.sqrt(int(prompt_root))
# print the square root of the number and give a farewell to the user
print('The square root of that number is', square_root, '! That\'s enough math for today. So long!')
