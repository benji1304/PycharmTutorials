# unicode
# A - Z 65 - 90
# a - z 97 - 122

# receive string, change to unicode, then change back
# enter string in Upper
# convert into unicode

orig_message = input("Enter your message in UPPER case: ")

secret_message = ""

for char in orig_message:
    secret_message += str(ord(char) - 23)


# for i in range(0, len(orig_message)):  # cycle through str, from start to length - 1, 1 at a time
#     secret_message += ord(orig_message[i])

print("\nSecret message is:", secret_message, end="")

norm_string = ""
for i in range(0, len(secret_message)-1, 2): # cycle through str, from start to length - 1, 2 at a time
    char_code = secret_message[i] + secret_message[i+1]
    norm_string += chr(int(char_code) + 23)

print("\nOriginal message is:", orig_message, end="")