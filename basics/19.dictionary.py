# Dictionary
# dictionaries are object of key:value pairs
# values of a dictionary must be immutable (string, number, tuple...)
# dictionaries are defined by "{}"
# they are like objects in JavaScript, but unlike objects there
# a dictonary value are in JSON-ish format:

user = {
    "account_name": "Tj",
    "real_name": "Thomas Johanson",
    "age": 18,
    "friends": ["Carla", "Cisco"],
    "is_active": False,
}


# Accessing values in Dictionary
# 1. Bracket notation
print(user["real_name"])

# but this can cause an exception if dict has no such key
# to safely get the value you can use the following .get() method


# 2. using the .get() method
# syntax: dict.get(key, default)
print(user.get("real_name"))

# when using get() method to look for non-existent key
# the method will then return None


# Modifying more values into dictionary
# we can modify existing or add new values like this:
user["age"] = 19
user["gender"] = "male"

# to remove a value use the "del" keyword
del user["real_name"]

print(user)


# Looping through dictonary
# 1. over all key-value pairs
for key, value in user.items():
    print(f"{key}: {value}")


# 2. only keys
for key in user.keys():
    print(key)


# 3. only values
for value in user.values():
    print(value)
