# For each question, I've written some setup code. Don't modify the setup code.
# Write your work underneath where it says "your work:" and of course add new lines if you need.
# The setup code usually contains variables.
# These varibles have example values; you should write the code as if you know the type, but don't know the exact values.

# ============== Question 0 ==============
print("Question 0:")

# Print all of the primitive types in Python that you know.

# your work:

print("int\nfloat\nstring\nboolean\nspecial")

# ============== Question 1 ==============
print("\nQuestion 1:") # side note: \n in a string means add a new line
x = 5

# Print "x is five" only if x is 5.
# Otherwise print nothing.

# your work:

if x == 5:
    print("x is five")

# ============== Question 2 ==============
print("\nQuestion 2:")
guitars = 3

# Print "Let's rock!" only if guitars is more than 4.
# Otherwise if guitars is more than 2, print "I need a few more guitars".
# Otherwise print "I need many more guitars".
# Hint: the greater than operator is >

# your work:

if guitars > 4:
    print("Let's rock!")
elif guitars > 2:
    print("I need a few more guitars")
else:
    print("I need many more guitars")

# ============== Question 3 ==============
print("\nQuestion 3:")
has_oranges = True
has_bananas = True

# 1. Print "I have fruit" only if has_oranges or has_bananas is true.
#    Otherwise print "I am hungry".
# 2. Print "I have oranges" if has_oranges is true.
# 3. Print "I have bananas" if has_bananas is true.

# your work:

if has_oranges or has_bananas:
    print("I have fruit")

    if has_oranges:
        print("I have oranges")
    if has_bananas:
        print("I have bananas")
else:
    print("I am hungry")

# ============== Question 4 ==============
print("\nQuestion 4:")
A = False
B = True

# 1. Print "pizza" only if A or B is true.
#    Otherwise print "lemon".
# 2. Print "fudge" if A is true.
# 3. Print "lasagne" if B is true.

# your work:

if A or B:
    print("pizza")

    if A:
        print("fudge")
    if B:
        print("lasagne")
else:
    print("lemon")

# ============== Question 5 ==============
print("\nQuestion 5:")
family_presents = 9
has_tree = True
decorations = 16
christmas_miracle = True

# The number of presents you'll receive from your family is given by the variable family_presents.
# Santa will only visit if we have a tree and we have at least 20 decorations, or if there is a christmas miracle.
# If Santa visits, the number of presents he'll give you will be half the number of decorations you have (rounded down).
# Print the total number of presents that you'll recieve.

# your work:

if has_tree and decorations >= 20 or christmas_miracle:
    print(family_presents + decorations//2)
else:
    print(family_presents)