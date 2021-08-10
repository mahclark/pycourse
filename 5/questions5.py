
# ============== Question 0 ==============
print("Question 0:")

# Which of the following are bad uses of inheritance?

# a)    Lion inherits from Animal.
# b)    Vector3 representing a 3D coordinate inherits from Vector2 (representing a 2D coordinate).
# c)    Son inherits from Father.
# d)    Waitress inherits from Employee.
# e)    Waitress inherits from Employer.
# f)    iPhone inherits from Phone.
# g)    CricketBat inherits from Cricket.
# h)    Planet inherits from Earth.

# your work:



# ============== Question 1 ==============
print("Question 1:")

# The class Vessel represents a vehicle which traverses across the sea.
# Each vessel has a name, an x position and a y position,
# hence you can find those 3 in the constructor which is done for you.
#
# a)    Write functions get_longitude and get_latitude which return
#       the x position and y position respectively.
#
# b)    Write a function at_sea which returns whether the vessel is at sea.
#       Below is map of the world, where ■ means land and ~ means sea.
#       The sea stretches infintely up and to the right.
#       Assume coordinates will be ints > 0.
#         ^
#         |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#       8 +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#         |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#       6 +■■■■■■■■■■■■■■■■■■■■~~~~~~~~~~~
#   y     |■■■■■■■■■■■■■■■■■■■■~~~~~~~~~~~
#       4 +■■■■■■■■■■■■■■■■■■■■~~~~~~~~~~~
#         |■■■■■■■■■■■■■■■■■■■■~~~~~~~~~~~
#       2 +■■■■■■■■■■■■■■■■■■■■~~~~~~~■~~~
#         |■■■■■■■■■■■■■■■■■■■■~~~~~~~~~~~
#       0 +---+---+---+---+---+---+---+--->
#         0   2   4   6   8   10  12  14
#                        x
#
# c)    Write a function describe which prints a string describing
#       the vessel's name, position and whether it's at sea.
#       E.g.:
#
# Name:
#     Position:   (x,y)
#     At sea:     True/False

class Vessel:

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    # your work:


# ============== Question 2 ==============
print("Question 2:")

# Write a class Plane which inherits Vessel.
#
# a)    Add a constructor which takes the parameters self, name, x, y and altitude.
#       The default value of altitude should be 0.
#       Remeber to call the super constructor.
#
# b)    Add a function get_altitude which returns the plane's altitude.
#
# c)    Override the function describe, so that it calls the super describe
#       and prints a further line with the altitude.

# your work:



# ============== Question 3 ==============
print("Question 3:")

# Write a class Boat which inherits Vessel.
#
# a)    Add a constructor which takes the parameters self, name, x, y.
#       The constructor should give the object two new variables:
#           has_holes = False
#           capsized = False
#       Remeber to call the super constructor.
#
# b)    Add a function set_holes which takes in a parameter.
#       The function should reassign the object's variable has_holes to the parameter.
#
# c)    Add a function capsize which sets the object's variable capsized to True.
#
# d)    Add a function is_sinking which returns a boolean.
#       It should return true if the boat is at sea and either has holes or is capsized.
#
# e)    Override the function describe, so that it calls the super describe
#       and prints a further line with whether the boat is sinking.

# your work:


# ============== Question 4 ==============
print("Question 4:")

# In a list, instantiate several Planes and Boats with different parameters.
# Itereate over the list and describe each one.
