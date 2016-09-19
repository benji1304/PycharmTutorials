# if age 5 go to kindergarten
# age 6 - 17 goes to grades 1 through 12
# if age is greater than 17 go to college
# 10 or less lines

# Receive age and store in age
age = eval(input("Enter age: "))


# if statement age is both greater than or equal and less than or equal to 18 Important
if (age < 5):
    print("Don't go to school2")
elif age == 5:
    print("Go to Kindergarten")
elif (age >= 6) and (age < 17):
    print("Grades 1 through 17")
elif (age >= 17) and (age <= 21):
    print("Go to college")
else:
    print("Leave school")