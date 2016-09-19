# Create a command line calculator
# vars num1 and num2 then an if statement for the operator

# take user input
num1, operator, num2 = input("Enter calculation: ").split()

# convert num1 num2 to ints
num1 = int(num1)
num2 = int(num2)

# setup calculator
if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1 + num2))
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))
elif operator == "%":
    print("{} % {} = {}".format(num1, num2, num1 % num2))
else:
    print("Use a proper operator next time")

