from tkinter import *

# Widget = A GUI element like button, input, label, images...just like HTML Tags
# Windows = A container that holds your widgets


window = Tk()  # Creates a root window

# Customizing the window
window.geometry("420x420")
window.title("Python GUI")
window.config(background="#999999")

# To change the icon, you must convert a image to photo image
# > icon = PhotoImage(file="path-to-the-file")
# > window.iconphoto(True, icon)


window.mainloop()  # Display the window
