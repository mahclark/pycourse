
# ============== Question 0 ==============
print("Question 0:")

# Describe the difference between a class and an object.

# your work:

# A class is a decription of an object in code.
# An object is an instance of a class.

# ============== Question 1 ==============
print("Question 1:")

# Below is a class definition of a product on sale in a store.
# Each product has a name and a price.
# When the store has a sale, the price gets reduced by a percentage of its current price.
# This is done using the function reduce_by.
# The parameter percent is a float between 0 and 1.
# Complete this function so it reduces the price correctly.

# E.g. if the price is 80.0 and percent is 0.1,
# the product's new price will be 72.0

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def reduce_by(self, percent):
        # your work:
        self.price *= 1 - percent

# ============== Question 2 ==============
print("Question 2:")

# Instantiate two products:
#   - a guitar with name="Guitar" and price=500
#   - a pencil with name="Pencil" and price=0.4
# The store has a sale of 20% off guitars and 50% of pencils.
# Code this change and print the final prices.

# your work:

guitar = Product("Guitar", 500)
pencil = Product("Pencil", 0.4)

guitar.reduce_by(0.2)
pencil.reduce_by(0.5)

print(guitar.price)
print(pencil.price)

# ============== Question 3 ==============
print("Question 3:")

# The class below represents the position of a boat in the sea.
#  a)   Each Pos should have an x and a y value which are set in the constructor from parameters.
#       Complete the constructor.
#
#  b)   Add a function called move, which adds
#       an x and y value to the current coordinates.
#
#  c)   Create a static method called poole_harbour,
#       which returns a Pos with coordinates (23, -17).
#
#  d)   Add a function called distance_to. It should take in a Pos as a parameter.
#       It should return the straight line distance from the current Pos to the other Pos.
#       Hint: use Pythagoras' theorem; prep 3pt2 tells you how to calculate the square root;
#       x to the power of 2 is x**2.

from math import sqrt

class Pos:
    # your work:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    @staticmethod
    def poole_harbour():
        return Pos(23, -17)

    def distance_to(self, pos):
        return sqrt((self.x - pos.x)**2 + (self.y - pos.y)**2)


# ============== Question 4 ==============
print("Question 4:")

# The class below represents a Boat in the sea.
#  a)   Each Boat should have a Pos which is set in the constructor from a parameter.
#       Complete the constructor.
#
#  b)   In the constructor, set the default value of
#       the position of the boat to be Poole Harbour.
#
#  c)   Add a function called distance_to_poole,
#       which returns the distance of the boat to Poole Harbour.

class Boat:
    # your work:

    def __init__(self, pos=Pos.poole_harbour()):
        self.pos = pos

    def distance_to_poole(self):
        return self.pos.distance_to(Pos.poole_harbour())

calais = Pos(104,21)
boat = Boat(calais)
print(boat.distance_to_poole())
