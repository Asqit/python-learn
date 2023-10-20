import os
import shutil

# os.remove = removes a file
# os.rmdir = delete a empty folder
# shutils.rmtree = delete a folder and it's contents (files...)

# os.getcwd() returns a working directory
path = os.getcwd() + "/io/test"

try:
    if os.path.isfile(path):
        os.remove(path=path)
    # os.rmdir(path=path) # empty folder
    shutil.rmtree(path=path)  # removes a folder and all it's files
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Folder cannot be deleted. (permission)")
except Exception as e:
    print(e)
else:
    print(path + " was successfully deleted")
