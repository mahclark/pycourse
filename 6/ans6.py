
# ============== Question 0 ==============
print("Question 0:")

# What are the time complexities (i.e. O notation) of the following:
# 
# a)    check if item in list
# b)    check if item in linked list
# c)    check if item in set
# d)    check if key in dictionary
# e)    check if value in dictionary
# f)    index list
# g)    index linked list
# h)    delete item in list
# i)    delete item in linked list (given the node to delete)
# j)    delete item in set
# k)    delete key/value pair in dictionary

# your work:



# ============== Question 1 ==============
print("Question 1:")

# Warm up question:

# Complete the function below so it returns True
# if a is in my_list, otherwise False.

# With n being the length of the list,
# what is the time complexity of your implementation?

def item_in_list(a, my_list):
    # your work:
    pass

# ============== Question 2 ==============
print("Question 2:")

# Complete the function below so it returns True
# if every item in items is in my_list, otherwise False.

# With n being the length of my_list and m being the length of items,
# what is the time complexity of your implementation?

def all_in_list(items, my_list):
    # your work:
    pass

# ============== Question 3 ==============
print("Question 3:")

# Create a class called Store.
# 
# a)    Add a constructor which takes in two parameters:
#           - items: a list of strings (the products on sale)
#           - prices: a list of floats (the prices of all products)
#       The items and prices have the same order.
#       I.e. the nth price corresponds to the nth item.
#
# b)    Add a function get_price which takes in one parameter:
#           - item: a string
#       The function should return the price of the item if it exists.
#       If the item doesn't exist, it should return None.
#       Think carefully about any preparation you can do in the constructor
#       to improve the efficiency of get_price.
#
# c)    What is the time complexity of the constructor?
#
# d)    What is the time complexity of get_price?

# your work:

class Store:

    def __init__(self, items, prices):
        self.prices = {}
        for item, price in zip(items, prices):
            self.prices[item] = price

    def get_price(self, item):
        return self.prices.get(item, None)

# ============== Question 4 ==============
print("Question 4:")

# An item in a list is unique if it's the only one in the list.
# Complete the function below so it returns the first unique item in the list.
# If there are no unique items in the list, it should return None.

# What is the time complexity of your implementation?

def first_unique(my_list):
    freq = {}
    for item in my_list:
        freq[item] = freq.get(item, 0) + 1

    for item in my_list:
        if freq[item] == 1:
            return item

    return None