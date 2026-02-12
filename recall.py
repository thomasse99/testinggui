import tkinter as tk
import random

root = tk.Tk()
image = tk.PhotoImage(file="ohyeah.gif")

def make_window():
    newwindow = tk.Toplevel(root)
    newwindow.geometry(f"200x180+{random.randint(40,1900)}+{random.randint(40,900)}")
    tk.Label(newwindow, image=image).pack()

root.geometry("200x200+400+400")
root.title("the window")
tk.Label(root, text="heres some text maybe").pack()

secondwindow = tk.Toplevel(root)
secondwindow.title("2nd window")
secondwindow.geometry("200x200+620+400")
tk.Label(secondwindow, text="This is the second window").pack()
tk.Label(secondwindow, image=image).pack()
tk.Button(text="make another window", command=make_window).pack()

root.mainloop()