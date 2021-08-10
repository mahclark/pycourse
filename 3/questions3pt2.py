
# ============== Question 0 ==============
print("Question 0:")

# In Python, you can use the functions max and min.
# For numbers x and y, max(x, y) returns the largest of the two.
# For iterable a, max(a) returns the largest value in a.
# min is used in the same way to find the smallest value.

# Complete the function below to return the minimax of 2 lists.
# Each list has a maximum value. The minimax is the smallest of the two maximums.

def minimax(list_A, list_B):
    # your work:
    pass

# ============== Question 1 ==============
print("\nQuestion 1:")

# In Python, you can access various mathematical functionality using the maths module.
# You can use this module by running:
import math
# Using Google, what is the URL for the official Python maths module documentation?
# The URL should start with https://docs.python.org

# your work:



# ============== Question 2 ==============
print("\nQuestion 2:")

# Using the documentation you found,
# explain what the functions math.ceil and math.floor do.
# Give an example value of x where math.floor(x) does not equal int(x).

# your work:



# ============== Question 3 ==============
print("\nQuestion 3:")

# To use functions from a module, you can either do:
math.ceil(1.2)
# or you can:
from math import ceil
ceil(1.2)

# Using the documentation, complete the function below to
# compute and return the sine of the square root of x.

def sine_square_root(x):
    # your work
    pass

# ============== Question 4 ==============
print("\nQuestion 4:")

# Find the official Python documentation for built in functions in Python.
# Here you can see many built in functions, some of which you should recognise, including:
# min(), max(), range(), enumerate(), zip(), float(), int(), round(), len(), and print()
# Read the documentation for sum().

# Using sum(), complete the function to return the average value of a list.

def average(my_list):
    # your work:
    pass


# ============== Question 5 ==============
print("\nQuestion 5:")

# In the documentation, you can find the sorted() method which takes an iterable and returns a sorted list.
# Numbers are sorted numerically, e.g. sorted([3, 1.4, 6, 4]) returns [1.4, 3, 4, 6]
# Strings are sorted alphabetically, e.g. sorted(["c","a","b"]) returns ["a","b","c"]

# If you specify key as a function, the list will be sorted
# on the results of each element applied to the function.

# E.g. to sort strings by their length, set key to be the function len.
# sorted(["looooooooong","short","medium"], key=len) returns ["short","medium","looooooooong"]


# Complete the function below to sort a list of strings by their last character and return it.
# E.g. ["tictac", "rhubarb", "zebra"] becomes ["zebra", "rhubarb", "tictac"]
# You should use sorted() and set key to be a lambda.
# Hint: remember you can index a string like a list.

def sort_by_last_letter(strings):
    # your work:
    pass

# ============== Question 6 ==============
print("\nQuestion 6:")

# Explain the difference between = and ==

# your work:



# ============== Question 7 ==============
print("\nQuestion 7:")

# Complete the function below to decrement the last value of a list by 100.

def decrement_last(numbers):
    # your work:
    pass

# ============== Question 8 ==============
print("\nQuestion 8:")

# The truth table below describes the function below that you should complete.
# The inputs are A and B and will be booleans or ints.
# (remember you can treat bools and ints the same)
# Return the correct value of x as an int according to the table.
# Hint: not inverts a boolean, e.g. not True equals False and not False equals True.
# Hint: != is the not equals comparator.

#  a | b || x
# ---|---||---
#  0 | 0 || 0
#  0 | 1 || 1
#  1 | 0 || 2
#  1 | 1 || 1

def compute_x_easy(a, b):
    # your work:
    pass

# ============== Question 9 ==============
print("\nQuestion 9:")

# Complete the function to return x as an int for the following truth table.

#  a | b | c || x
# ---|---|---||---
#  0 | 0 | 0 || 0
#  0 | 0 | 1 || 0
#  0 | 1 | 0 || 1
#  0 | 1 | 1 || 2
#  1 | 0 | 0 || 0
#  1 | 0 | 1 || 1
#  1 | 1 | 0 || 3
#  1 | 1 | 1 || 3

def compute_x_hard(a, b, c):
    # your work:
    pass

# ============== Question 10 ==============
print("\nQuestion 10:")

# Write some Christmasy code!
# Be creative.
# Try to use much of what we've learnt in the course so far (basics, functions, lists & loops).
# Below is my Christmasy code; call make_it_snow() to see what it does.
# You don't necessarily have to print a scene like I did, but you can if you like.

def make_it_snow():
    scene = []

    # Yes you can define a function inside a function
    def set_at(scene, x, y, value):
        # This function takes a list of strings (scene) and sets the character at coordinates (x,y) to value
        scene[y] = scene[y][:x] + value + scene[y][x+1:]

    # Side note: if you need a for loop but don't need the variable, it's conventional to use _
    for _ in range(11):
        scene.append(" "*33)

    for y, row in enumerate(scene):
        if y % 2 == 0:
            xs = range(1, len(row), 6)
        else:
            xs = range(4, len(row), 6)

        for x in xs:
            set_at(scene, x, y, "*")

    # Strings are also iterables
    for i, char in enumerate("Merry Christmas!"):
        set_at(scene, 9+i, 5, char)

    scene = ["="*33] + scene + ["="*33]

    # The next line joins all the strings in the list together, separated by new lines
    result = "\n".join(scene)
    print(result)

# your work:
