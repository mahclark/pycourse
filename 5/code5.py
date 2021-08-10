class Animal:

    def __init__(self):
        super().__init__()
        print("Create an animal")

    def speak(self):
        print("???")

class ThingWithWings:

    def __init__(self):
        print("Create a thing with wings")

    def flap(self):
        print("flap flap flap")

class Lion(Animal):

    def speak(self, loud=False):
        if loud:
            print("ROOOOAAAHHHH")
        else:
            print("growlll")

class Walrus(Animal):

    def __init__(self):
        super().__init__()
        print("Create a walrus")

class Flamingo(Animal, ThingWithWings):
    pass

flamingo = Flamingo()
flamingo.speak()
flamingo.flap()

# animal = Animal()
# lion = Lion()
# walrus = Walrus()

# animals = [animal, lion, walrus]

# for a in animals:
#     a.speak()