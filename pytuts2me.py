# we'll provide different outputs dependent on age
# 1 - 18 > Important
# 21, 50, > 65 > Important
# All others > Not Important

# Receive age and store in age
age = eval(input("Enter age: "))

# and : If both are true it returns true
# or : If either are true it returns true
# not : Converts true to false


# if statement age is both greater than or equal and less than or equal to 18 Important
if (age >= 1) and (age <= 18):
    print("Important birthday")


# if age is 21 or 50 important
elif (age == 21) or (age == 50):
    print("Important birthday")

# we check if age is less than 65 and then convert true to false
elif not (age < 65):
    print("Important birthday")

# else not important
else:
    print("Not important birthday")