
# ============== Question 0 ==============
print("Question 0:")

# Write a for loop which prints every even number between 1 and 9:

def for_loop_even():
    # your work:
    for i in range(2, 10, 2):
        print(i)

for_loop_even()

# ============== Question 1 ==============
print("Question 1:")

# Write a while loop which prints every even number between 1 and 9:

def while_loop_even():
    # your work:
    i = 2
    while i < 9:
        print(i)
        i += 2

while_loop_even()

# ============== Question 2 ==============
print("Question 2:")

# For loops iterate over iterables.
# In the function below, write two for loops, each using a different type of iterable.
# Each for loop should print the numbers 1 to 10 inclusive.

def iterate_twice():
    # your work:
    for i in range(1,11):
        print(i)

    for i in [1,2,3,4,5,6,7,8,9,10]:
        print(i)

iterate_twice()

# ============== Question 3 ==============
print("Question 3:")

# Complete the function below so it returns a list of all positive integers less than x.

def all_less_than(x):
    # your work:
    mults = []
    for i in range(1, x):
        mults.append(i)
    return mults

print(all_less_than(5))

# ============== Question 4 ==============
print("Question 4:")

# Complete the function below so it returns a list of all positive integers less than x which are a multiple of 3.

def multiple3_less_than(x):
    # your work:
    mults = []
    for i in range(3, x, 3):
        mults.append(i)
    return mults

print(multiple3_less_than(20))

# ============== Question 5 ==============
print("Question 5:")

# Complete the function below so it returns a list of all positive integers less than x which are a multiple of a.

def multiple_less_than(x, a):
    # your work:
    mults = []
    for i in range(a, x, a):
        mults.append(i)
    return mults

print(multiple_less_than(20,6))

# ============== Question 6 ==============
print("Question 6:")

# Using the function multiple_less_than which you completed above,
# complete the function below so it returns a list of lists.
# The list should contain x-1 elements.
# The 1st element should be a list of all multiples of 1 less than x.
# The 2nd element should be a list of all multiples of 2 less than x.
# The nth element should be a list of all multiple sof n less than x.

# E.g.
# if x = 5, we should return:
# [[1,2,3,4], [2,4], [3], [4]]

def all_multiples_less_than(x):
    # your work:
    all_mults = []
    for i in range(1, x):
        all_mults.append(multiple_less_than(x, i))
    return all_mults

print(all_multiples_less_than(6))

# ============== Question 7 ==============
print("Question 7:")

# Complete the function below so it returns a list of ints.
# Add together all the elements of each list into a new list and return it.
# I.e. the nth element should equal the nth element of list_A plus the nth element of list_B.
# If the lists are not the same size,
# the remaining items of the longer list should be ignored.

def add_lists(list_A, list_B):
    # your work:
    added = []
    for a, b in zip(list_A, list_B):
        added.append(a + b)
    return added

print(add_lists([5,5,5], [2,-5,6,14,7]))
