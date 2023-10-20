# Code documentation is important and so it does exist in python


def add(a: int, b: int) -> int:
    """
    Add two arguments
    Arguments:
        a: an integer
        b: an integer
    Returns:
        The sum of the two arguments
    """

    return a + b


# One quite important and useful fact to know is that
# Python does store your documentation inside "__doc__" property of your function
# so that you can use in-build "help()" function
help(add)

print(add(2, 2))

# simply print the property on your own
print(add.__doc__)
