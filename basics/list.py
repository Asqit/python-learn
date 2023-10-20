# Lists
# lists is an ordered collection of items

# here we declare a list of numbers. The length is limitless
# but the longer the slower the program will be
numbers = [1, 2, 3, 4, 5, 6, 7]

# we can access an element by using square brackets
# indexing in python is very serious thing
# and it's syntax is like this: [start:stop:step]
# start -   starting position
# stop  -   up to but not including "stop" element
# step  -   by how many we slicing
# we can omit each parameter by continuing without value but ":"
print(numbers[:3:1])  # all numbers to 3 but not including 3
print(numbers[0])  # just the first element


# Unpacking a list
# in javascript this is called descturcturing, but in python we call it unpacking
# we basically assign values from list to variables
names = ["Andrew", "Johnatan", "Liss", "Ludmila"]

# this is how you unpack things in python
# the variables on the left must be of the size of the list on the right
# if not you must use the "*" operator to create a sublist of whats left
andrew, liss, *others = names

# you might think that liss variable is gonna have a "Liss" value
# but actually it does have a "Johnatan" as the value
# that's because we go over indexes so liss must be a third variable
# andrew, johnatan, liss, *others, names
# this way the liss would be "Liss"
print(liss)

# Also notice the asterisk on the "others" variable
# it tells python to unpack what's left of the list and assign it
# to the variable
print(others)


# Then again if you try to unpack less variables then there is values in the list
# you'll get an error: ValueError: too many values to unpack

# warning, the following code raises an exception
# one, two = numbers


# looping over
for number in numbers:
    print(number)


# looping over with index
for i, name in enumerate(names):
    print(f"{i}: {name}")


# Finding an index of element
# to find an index you can use the ".index()" method on type list
index_of_andrew = names.index("Andrew")

# but it can also throw an exception:
# ValueError: 'Value' is not in list


# but we can safely get the index like this:
number = 120

if number in numbers:
    result = numbers.index(number)
    print(f"The number {number} has an index of {result}")
else:
    print(f"{number} does not exist in the targeted list")


# just like in javascript we have methods like:
# .filter, .map...but they are globaly available
# rather than object related
# but unlike in javacript, they return an iterator
# so you must then create a new list by calling:
# list = list(map(fn, list))


def double(value):
    return value * 2


doubled = map(double, numbers)

# or in more javascripty way:
# doubled = doubled.map(v => v * 2)
doubled = map(lambda value: value * 2, numbers)

print(list(doubled))


# Filtering:
def get_even(value: int) -> int or None:
    if value % 2 != 0:
        return
    else:
        return value


even_numbers = filter(get_even, numbers)
even_numbers = filter(lambda v: v % 2 == 0, numbers)

print(list(even_numbers))
