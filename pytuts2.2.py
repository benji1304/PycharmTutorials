# your_float = input("Enter a float: ")
#
# your_float = float(your_float)
#
# print("Your number rounded to 2 dp: {:.2f}".format(your_float))

# Have the user enter their investment amount and expected interest
# each year their investments will increase by original + investment * interest rate
# print ou thte earnings after a 10 year period


# Ask the user for investment amount and interest
invest = input("How much to invest: ")
interest = input("What is the Interest Rate? ")

# Convert to float
invest = float(invest)
# Convert value to a float and round the percentage rate by 2 digits
interest = float(interest) * 0.01

for i in range(10):
    invest = invest + (invest * interest)

# output
print("Investment after 10 years : £{:.2f}".format(invest))