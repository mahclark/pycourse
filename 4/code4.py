class Pos:

    x = 5
    y = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

pos = Pos(5, 8)
# print(pos.x, pos.y)

pos.move(5, -1)
# print(pos.x, pos.y)

class TestResults:

    # results = [99,13,56]

    def __init__(self, course):
        self.course = course
        self.results = [99,13,56]

    def set_student_score(self, i, score):
        self.results[i] = score

coding_results = TestResults("coding")
biology_results = TestResults("biology")

coding_results.set_student_score(0, 22)
# print(coding_results.results)
# print(biology_results.results)

class Animal:

    def __init__(self, species):
        self.species = species

    @staticmethod
    def create_lion():
        return Animal("Lion")

cat = Animal("Cat")
lion = Animal.create_lion()

print(cat.species)
print(lion.species)