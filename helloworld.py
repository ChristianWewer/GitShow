print("hello world!")

print("What is your name?")
name = get_user_input()
print("Hello {}".format(name))



def get_user_input():
	""" This functions gets user input and retuns it as a string """
	return input(">")