# # single line comment
# '''
# multi line comment
# '''
#
# # Ask the user to input their name and assign it to a variable named name
#
# name = input('What is your name? ')
#
# # Print out Hello followed by their name entered
#
# print('Hello',name)
#
# # example variable name: the_name_1
#

'''
Ex 1
'''

# Ask the user to input 2 values and store them in variables num1 and num2
num1, num2 = input('Enter 2 numbers: ').split()

# Convert strings to regular numbers Integer
num1 = int(num1)
num2 = int(num2)

# Add the balues entered and store in sum
sum = num1 + num2

# Subtract values and store in a variable difference
difference = num1 - num2

# multiply the values and store in product
product = num1 * num2

# divide the values and store in quotient
quotient = num1 / num2

# modulus the values and store in remainder
remainder = num1 % num2

# Print the results
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))

