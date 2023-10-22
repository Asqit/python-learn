# Sometimes we don't have implementation of certain part of code just yet
# but we want to write a placeholder and skip the implementation for now
# to do so in normal language we would just leave it closed by pair of {}
# but in python we have the "pass" keyword


def unfinished_code():
    pass


user_input = input("True or False? ")

if bool(user_input):
    print("Hey ya")
else:
    pass


class _experimental_Animal:
    """Experimental: does not have implementation!"""

    pass
