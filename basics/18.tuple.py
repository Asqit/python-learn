# tuples - collection which is ordered and immutable
# they are used to group together related data

student = ("Any", 22, "Male")

# .count method will count every occurrence of specific value
number_of_occurrences = student.count("Male")

# returns an index of certain value
# or throws exception (ValueError: x not in tuple)
student.index("Male")

# we can loop over all properties of tuple
for prop in student:
    print(prop)

# we can also check if property is inside of tuple
if "Andy" in student:
    print("Andy is student")