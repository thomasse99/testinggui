import tkinter as tk

root = tk.Tk()

tk.Button(text="Button").grid(row=1, column=1)
tk.Button(text="Button").grid(row=1, column=2)
tk.Button(text="Button").grid(row=2, column=1)

root.mainloop()