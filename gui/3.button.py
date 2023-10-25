import tkinter as tk

count = 0


def click() -> None:
    global count
    count += 1


root = tk.Tk()
root.geometry("120x64")

button = tk.Button(
    root,
    text="Click me, nigga!",
    command=click,
    font=("Menlo", 12),
    fg="#fff",
    bg="green",
    activebackground="black",
    activeforeground="white",
    # state="disabled",
)
button.pack()

count_label = tk.Label(root, text=count)
count_label.pack()

root.mainloop()
