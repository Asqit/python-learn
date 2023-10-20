# Detecting whenever file exist or not
import os

FILE_PATH = "C:\\Users\\ondre\\Desktop\\test"

if os.path.exists(FILE_PATH):
    print("That location exists!")
    if os.path.isfile(FILE_PATH):
        print("That is a file!")
    elif os.path.isdir(FILE_PATH):
        print("That is a directory")
else:
    print("That location does not exist!")
