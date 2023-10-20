# Reading a file in Python

FILE_PATH = "C:\\Users\\ondre\\Desktop\\test\\test.txt"

# the "with" keyword automatically closes a file
# to prevent memory overflow
try:
    with open(FILE_PATH + "x") as file:
        print(file.read())

    print(file.closed)
except FileNotFoundError:
    print("File not found")
