import os

SOURCE = os.getcwd() + "\\io\\sample.txt"
TARGET = "C:\\Users\\ondre\\Desktop\\test\\test.txt"

try:
    if os.path.exists(TARGET):
        print("file already exists")
    else:
        # You can also move a folder like this
        os.replace(SOURCE, TARGET)
        print(SOURCE + " was moved")
except FileNotFoundError:
    print(SOURCE + " was not found")
except Exception as e:
    print(e)
