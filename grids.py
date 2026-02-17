import tkinter as tk

root = tk.Tk()

root.geometry("+500+400")

def get_name(event=None):
    username = name.get()
    if not username:
        return None
    for widget in root.winfo_children():
        widget.destroy()
    tk.Label(root, text=f"Hi there {username}", font=("font", 15)).pack(pady=10,padx=10)
    

tk.Label(root, text="Enter Name:").grid(row=0,column=1, pady=8, padx=8)
name = tk.Entry(root)
name.grid(row=0, column=2, pady=8, padx=8)
name.bind("<Return>", get_name)
enter_button = tk.Button(root, text="Enter",command=get_name)
enter_button.grid(row=1,column=1,columnspan=2, pady=8, padx=8)

root.mainloop()