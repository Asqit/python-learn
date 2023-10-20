# This is an example of Python module
# each of the follwing code structures are public/exported
# Python does not use private parts of the code, but by convention
# python developers use "_" to prefix a private class/func/var...


# An example of "private" or non-exported function
def _non_exported_private_function() -> None:
    print("I am private....LEAVE ME ALONE!")


# Regular function, that are "exported"
def hello() -> None:
    print("Hello!")


def bye() -> None:
    print("bye!")
