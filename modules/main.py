# Modules
# A file containing python code. It may contain functions, classes and more
# it is used to separate a program into smaller pieces
import messages

# or we can use the alias import:
# > import messages as msg

# or just the functions we need
# > from messages import hello, bye

# or all
# > from messages import *

messages.hello()


messages.bye()

# We can still access private functions
# but as long as they are prefixed with "_"
# it is better to leave them alone
messages._non_exported_private_function()

# in-build modules
help("modules")
