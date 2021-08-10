# pass is a command in Python which does nothing.
# I've included pass here because every function needs something else it will throw an error.
# When writing a solution, if you see pass, feel free to delete it.
# Beneath the functions that form your answer, feel free to call your function with parameter values of your choice to check your code works.

# ============== Question 0 ==============
print("Question 0:")

# Write a function which doubles a number. Your function should take in an int or a float and return a float.

def double(x):
    # your work:
    pass

# ============== Question 1 ==============
print("\nQuestion 1:")

# Using += in your solution, answer question 5 from yesterday's homework.
# Instead of printing the total number of presents, return it as an int.

def count_xmas_presents(family_presents, has_tree, decorations, christmas_miracle):
    # your work:
    pass

# ============== Question 2 ==============
print("\nQuestion 2:")

# Adjust the function below so that:
#    - the default value of vehicle is "bike"
#    - the default value of num_wheels is 2

# your work:
def number_wheels(vehicle, num_wheels):
    return "A " + vehicle + " has " + str(num_wheels) + " wheels."

# ============== Question 3 ==============
print("\nQuestion 3:")

# Write a function which multiplies x by 2 and applies the result to the mystery function.
# Assume the mystery function accepts one parameter.
# This function should return None.

def double_mystery(x, mystery_func):
    # your work:
    pass

# ============== Question 4 ==============
print("\nQuestion 4:")

# Write a function which returns a lambda.
# The lambda should multiply a number by 5.

def create_lambda():
    # your work:
    pass

# ============== Question 5 ==============
print("\nQuestion 5:")

def santa_visits(present_func, cookie_func):
    presents = 8
    cookies = 5

    print("Before Santa visited, there were " + str(presents) + " presents under the tree\n"
        + "and there were " + str(cookies) + " cookies on the plate.")

    presents = present_func(presents)
    cookies = cookie_func(cookies)

    print("After Santa visited, there were " + str(presents) + " presents under the tree\n"
        + "and there were " + str(cookies) + " cookies on the plate.")

# Above I have defined a function called santa_visits. Do not modify this function. Try to read and understand it.
# Complete the function below so it calls the function above.
# You should call the function with two lambdas:
#     - The first lambda should increase the number of presents under the tree by num_presents.
#     - The second lambda should half the number of cookies on the plate (rounded down).

def make_santa_visit(num_presents):
    # your work:
    pass
