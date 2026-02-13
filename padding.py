import tkinter as tk

root = tk.Tk()

tk.Button(text="Text is here").pack(padx=30,pady=10)
tk.Button(text="Text is also here").pack(ipadx=30,ipady=10)

root.mainloop()