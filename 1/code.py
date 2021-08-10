def describe(animal="Seal", name="Wendy"):
	return "This " + animal + " is called " + name + "."

def double(x):
	return 2*x


promote = lambda name: name + " Sir"
# print(promote("Max"))

def do_maths(func, x):
	return func(x)


def decribe_guitar(guitars):

	if guitars > 4:
	    print("Let's rock!")
	elif guitars > 2:
	    print("I need a few more guitars")
	else:
	    print("I need many more guitars")