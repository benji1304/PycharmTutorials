# how tall is the tree?
# how many rows!

# Use 1 While and 3 For Loops
# 4 spaces : 1 hash
# 3 spaces : 3 hash
# 2 spaces : 5 hash
# 1 space  : 7 hash
# 0 spaces : 9 hash
# top and bottom match hash

# TODO
# 1 Decrement spaces by 1 each time through loop
# 2 Increment hashes by 2 each loop
# 3 Save spaces to the stump (and top?) by calculating tree height - 1
# 4 Decrement from tree height until =  0
# 5 print spaces and then hash for each row
# 6 print stump spaces and then hash


# Ask for Number of Rows
tree_height = input("How tall is the tree? ")
# Convert rows to Int
tree_height = int(tree_height)

# Get starting spaces for Top of the tree
spaces = tree_height - 1

# There is 1 hash to start that will be incremented
hashes = 1 #always starts at 1 at the top

# Save stump spaces until later
stump_spaces = tree_height - 1  # same as spaces var above

# make sure the right number of rows are printed
while tree_height != 0:


# print the spaces
# end="" #stops new line
    for i in range(spaces):
        print(' ',end="")

# print the hash
    for i in range(hashes):
        print('#', end="")

# NewLine after each row printed
    print()

# Spaces is decremented -1 per row
    spaces -= 1

# Hash is increment +2 per row
    hashes += 2

# Decrement tree height to jump out of loop
    tree_height -= 1

# print spaces before stump on bottom
for i in range(stump_spaces):
    print(' ',end="")

print("#")
