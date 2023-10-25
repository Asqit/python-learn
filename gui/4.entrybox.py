import tkinter as tk


def submit():
    username = entry.get()
    print(f"Hello {username}")


def delete():
    entry.delete(0, len(entry.get()))


def backspace():
    length = len(entry.get())
    entry.delete(length - 1, length)


def is_gay():
    print(f"Is Gay: {checkbox_value}")


root = tk.Tk()
root.title("Login")

entry = tk.Entry(root, font=("menlo", 10), show="*")
entry.pack(side="left")

submit = tk.Button(root, text="submit", command=submit)
submit.pack(side="right")

delete = tk.Button(root, text="delete", command=delete)
delete.pack(side="right")

backspace = tk.Button(root, text="backspace", command=backspace)
backspace.pack(side="right")


checkbox_value = 0
checkbox = tk.Checkbutton(
    root, text="Are you gay?", variable=checkbox_value, command=is_gay
)
checkbox.pack(side="bottom")

root.mainloop()
