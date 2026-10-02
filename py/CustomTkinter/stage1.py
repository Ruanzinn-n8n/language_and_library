import customtkinter as ctk

window = ctk.CTk()
window.geometry("500x300")

# Exercise 1 - button
"""label = ctk.CTkLabel(window, text="DevBoard")
label.pack()

def printText():
    print("Button clicked!")

btn = ctk.CTkButton(window, text="Click here", command=printText)
btn.pack()
"""

# Exercise 2 - Button changing label
"""label = ctk.CTkLabel(window, text="Hi!")
label.pack()

def buttonclick():
    label.configure(text="Button clicked!")
    window.after(2000, lambda: label.configure(text="Hi!"))

btn = ctk.CTkButton(window, text="CHANGE TEXT", command=buttonclick)
btn.pack()
"""

# Exercise 3 - Input text
"""label = ctk.CTkLabel(window, text="Insert your name:")
label.pack()

insert = ctk.CTkEntry(window)
insert.pack()

def printName():
    name = insert.get()
    print(name)
    l_name = ctk.CTkLabel(window, text=f"Hello {name}!")
    l_name.pack()

confirm = ctk.CTkButton(window, text="Confirm", command=printName)
confirm.pack()
"""

# Exercise 4 - Grid
name = ctk.CTkLabel(window, text="Name:  ")
name.grid(row=0, column=0)

inputname = ctk.CTkEntry(window)
inputname.grid(row=0, column=1)

age = ctk.CTkLabel(window, text="Age:  ")
age.grid(row=1, column=0)

inputage = ctk.CTkEntry(window)
inputage.grid(row=1, column=1)

window.mainloop()