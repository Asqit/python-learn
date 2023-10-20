# Tuples
# tuples are like a list, but they cannot change so in short a tuple is immutable list

rgb = ("red", "green", "blue")

print(rgb[0])
print(rgb[1])
print(rgb[2])


# an exception will be raised:
# TypeError: 'tuple' object does not support item assignment
rgb[0] = "yellow"
