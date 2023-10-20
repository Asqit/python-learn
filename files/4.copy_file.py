# Functions of shutil:
# 1. copyfile(src, dest) = copies contents of a file
# 2. copy(src, dest) = copyfile() + permission mode + destination can be a directory
# 3. copy2(src, dest) = copy() + copies metadata
import shutil


shutil.copyfile(
    "C:\\Users\\ondre\\Desktop\\test\\test.txt",
    "C:\\Users\\ondre\\Desktop\\test\\copy.txt",
)
