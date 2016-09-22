# Handling errors on input

while True:
    try:
        number = int(input("What is your number? "))
        break
    except ValueError:
        print("You didn't enter a number! ")

    except:
        print("An unknown error occurred")

print("Thank you for entering a number")

print(number)

