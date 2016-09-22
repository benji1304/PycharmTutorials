# print(type(3))
# print(type(3.14))
# print(type("2"))

samp_string = "This is a very important string"

print(samp_string[-1]) #last character
print(samp_string[3+5]) # char 8

print("Length", len(samp_string))

print(samp_string[0:4]) # slices a part of string

print(samp_string[10:]) # slices a from point to end

print(samp_string * 2)

num_string = str(4) # set number as str

for char in samp_string:
    print(char)

for i in range(0, len(samp_string)-1, 2): # cycle through str, from start to length - 1, 2 at a time
    print(samp_string[i] + samp_string[i+1] ) #prints chars in pairs

# unicode
# A - Z 65 - 90
# a - z 97 - 122
#converting unicode to and from text
print("A = ", ord("A"))
print("65 = ", chr(65))

