FILE_PATH = "C:\\Users\\ondre\\Desktop\\test\\created.txt"

text = """Hello World!
My name is Andrew and I am Czech
I am a web developer and I like cars, computer games
"""

# The second argument is for mode
# r = read
# w = write
# a = append
with open(FILE_PATH, "w") as file:
    file.write(text)
