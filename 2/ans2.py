
# ============== Question 0 ==============
print("Question 0:")

# Explain the difference between a tuple and a list.

# your work:

# tuples use (); lists use []
# tuples are immutable i.e. you cannot modify an existing tuple; lists are mutable
# tuples are hashable; lists are not

# ============== Question 1 ==============
print("Question 1:")

# Complete the function below to return a list of 17 string values.
# Each value should be "hi".

def make_list_of_17():
    # your work:
    return ["hi"]*17

print(make_list_of_17())

# ============== Question 2 ==============
print("Question 2:")

# Complete the function below.
# i is an int which refers to an index of the list
# my_list is a list of numbers
# the function should set the value at index i in the list to 5

def set_index_to_5(i, my_list):
    # your work:
   my_list[i] = 5

a = [1,2,3]
set_index_to_5(1, a)
print(a)

# ============== Question 3 ==============
print("Question 3:")

# Complete the function below.
# i is an int which refers to an index of the list
# my_list is a list of numbers
# the function should double the value at index i in the list

def double_at_index(i, my_list):
    # your work:
    my_list[i] *= 2

a = [1,2,3]
double_at_index(2, a)
print(a)

# ============== Question 4 ==============
print("Question 4:")

# Complete the function below.
# The function should change the first value of my_list to "first".
# It should return a tuple of two values:
#   - the original list
#   - the list with the first value changed to "first"

def change_first_value(my_list):
    # your work:
    new_list = my_list.copy()
    new_list[0] = "first"

    return (my_list, new_list)

print(change_first_value([1,2,3]))

# ============== Question 5 ==============
print("Question 5:")

# Complete the function below.
# The function takes in two values, a and b, and a list.
# The function should return true if both values are in the list,
# otherwise false.

def both_in_list(a, b, my_list):
    # your work:
    return a in my_list and b in my_list

print(both_in_list(1, 2, [1,2,3]))

# ============== Question 6 ==============
print("Question 6:")

# If you index a list using an int which is too high or too low,
# it will throw an error.
# If you use an index less the zero, then it indexes from the right hand side.
# E.g. my_list[-1] is the last value and my_list[-2] is the second last value.
# Complete the function to return a tuple of the largest and smallest integer
# indexes that you can use on my_list without it throwing an error.
# Hint: remember len(my_list) gets the length of the list.

# Example:
# if my_list = ["elephant", "cactus", "badger"]
# then the largest index you can use is 2
# and the smallest index you can use is -3
# so the function should return (2, -3)

def max_min_index(my_list):
    # your work:
    return (len(my_list) - 1, -len(my_list))

print(max_min_index([]))