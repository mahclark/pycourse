
# ============== Question 0 ==============
print("Question 0:")

# Write a function which doubles a number. Your function should take in an int or a float and return a float.

def double(x):
    # your work:
    return float(2*x)

print(double(5))
# ============== Question 1 ==============
print("\nQuestion 1:")

# Using += in your solution, answer question 5 from yesterday's homework.
# Instead of printing the total number of presents, return it as an int.

def count_xmas_presents(family_presents, has_tree, decorations, christmas_miracle):
    # your work:
    total_presents = family_presents
    if has_tree and decorations >= 20 or christmas_miracle:
        total_presents += decorations//2
    return total_presents

print(count_xmas_presents(0, False, 0, False))
# ============== Question 2 ==============
print("\nQuestion 2:")

# Adjust the function below so that:
#    - the default value of vehicle is "bike"
#    - the default value of num_wheels is 2

# your work:
def number_wheels(vehicle="bike", num_wheels=2):
    return "A " + vehicle + " has " + str(num_wheels) + " wheels."

print(number_wheels())
# ============== Question 3 ==============
print("\nQuestion 3:")

# Write a function which multiplies x by 2 and applies the result to the mystery function.
# Assume the mystery function accepts one parameter.
# This function should return None.

def double_mystery(x, mystery_func):
    # your work:
    mystery_func(2*x)

double_mystery(4, print)
# ============== Question 4 ==============
print("\nQuestion 4:")

# Write a function which returns a lambda.
# The lambda should multiply a number by 5.

def create_lambda():
    # your work:
    return lambda x: x*5

print(create_lambda())
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

# Above I have defined a function called santa_visits. Do not modify this function.
# Complete the function below so it calls the function above.
# You should call the function with two lambdas:
#     - The first lambda should increase the number of presents under the tree by num_presents.
#     - The second lambda should half the number of cookies on the plate (rounded down).

def make_santa_visit(num_presents):
    # your work:
    santa_visits(
        lambda x: x + num_presents,
        lambda x: x//2
    )

make_santa_visit(5)