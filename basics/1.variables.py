# variable = a container for certain value. Behaves as the value that it controls.

# Strings - represents a string of characters
message = "Hey, Mom"
emoji = "❤️"

full_message = message + " " + emoji

print(full_message)
print(type(full_message))

# Int - stores only whole numbers
age = 21

# there is no automatic casting like in JS
# without parsing the "1" we would get type error
age += int("1") 

print(age)
print(type(age))

# Float - numbers with decimal portion
height = 180.5

print(f"I am {height}cm tall")
print(type(height))

# Boolean - only True of False
isHuman = True 

print(isHuman)
print(type(isHuman))