from tkinter import *


root = Tk()
root.geometry("420x420")

label = Label(
    root,
    text="Ahoj, Světe!",
    font=("Arial", 40, "bold"),
    fg="green",
    bg="#000",
    relief=RAISED,
    bd="10",
    padx=12,
    pady=12,
)
# label.place(x=0, y=0)
label.pack()

root.mainloop()
