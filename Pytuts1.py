# Problem : Receive miles and convert to kilometers
# kilometers = miles * 1.60934
# Enter Miles 5
# 5 miles = xxxx (8.04 km)

# Take user input of the number of miles
miles = input('Enter the number of miles: ')

# convert to integer
miles = int(miles)

# convert miles to km
km = miles * 1.60934



# print string and result to screen
#print(miles,' miles = ', km)
print("{} miles = {} kilometers".format(miles, km))