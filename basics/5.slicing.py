# creating substrings by extracting elements from another string
# - indexing via [] or slice()
# - indexing has three optional parameters: [start:stop:step]

name = "Andrew Tuček"

first_name = name[0:6:1]
last_name = name[7:len(name)]

print(first_name)
print(last_name)

# it is possible to omit each indexing parameter
# but I consider it a bad practice
# yet sometimes it is needed like in this case
funky_name = name[::2]
print(funky_name)

# it is possible to reverse a string like this
reversed_name = name[::-1]
print(reversed_name)

# slice function
# it has the same parameters as indexing
# but instead of using ":" as delimiter we use ","
website = "http://guthib.com"

slice = slice(7, -4)
print(website[slice])
