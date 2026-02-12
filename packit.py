import tkinter as tk

root = tk.Tk()

root.geometry("200x200+400+400")

tk.Button(root, text="button").pack()

tk.Label(root, text="Hi").pack(side="left")
tk.Label(root, text="There!").pack(side="right")

tk.Checkbutton(root, text="Please click me").pack(side=tk.BOTTOM)

root.mainloop()