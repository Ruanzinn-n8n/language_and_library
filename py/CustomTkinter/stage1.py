import customtkinter as ctk

window = ctk.CTk()
window.geometry("500x300")

# Exercise 1 - button
label = ctk.CTkLabel(window, text="DevBoard")
label.pack()

def printText():
    print("Button clicked!")

btn = ctk.CTkButton(window, text="Click here", command=printText)
btn.pack()


# Exercise 2 - Button changing label
label = ctk.CTkLabel(window, text="Hi!")
label.pack()

def buttonclick():
    label.configure(text="Button clicked!")
    window.after(2000, lambda: label.configure(text="Hi!"))

btn = ctk.CTkButton(window, text="CHANGE TEXT", command=buttonclick)
btn.pack()


# Exercise 3 - Input text
label = ctk.CTkLabel(window, text="Insert your name:")
label.pack()

insert = ctk.CTkEntry(window)
insert.pack()

l_name = ctk.CTkLabel(window, text="")
l_name.pack()
def printName():
    name = insert.get()
    print(name)
    l_name.configure(text=f"Hello {name}!")

confirm = ctk.CTkButton(window, text="Confirm", command=printName)
confirm.pack()


# Exercise 4 - Grid
frame = ctk.CTkFrame(window, width=300, height=200).place(x=100, y=50)

name = ctk.CTkLabel(frame, text="Name:  ")
name.grid(row=0, column=0)

inputname = ctk.CTkEntry(frame)
inputname.grid(row=0, column=1)

age = ctk.CTkLabel(frame, text="Age:  ")
age.grid(row=1, column=0)

inputage = ctk.CTkEntry(frame)
inputage.grid(row=1, column=1)

confirm = ctk.CTkButton(frame, text="Confirm")
confirm.grid(row=2, column=1)
# for some reason the widgets dont stayed in the frame. attempt fail in try to do more LOL

# Exercise 5 - Little DevBoard
label = ctk.CTkLabel(window, text="DevBoard")
label.grid(row=0, column=0)

key = ctk.CTkLabel(window, text="Key:  ")
key.grid(row=1, column=0)

inputkey = ctk.CTkEntry(window)
inputkey.grid(row=1, column=1)

short = ctk.CTkLabel(window, text="Short:  ")
short.grid(row=2, column=0)

inputshort = ctk.CTkEntry(window)
inputshort.grid(row=2, column=1)

def send():
    k = inputkey.get()
    s = inputshort.get()
    print("Register Sucess")
    print(f"Key: [{k}]\nShort: [{s}]")

register = ctk.CTkButton(window, text="Register", command=send)
register.grid(row=2, column=1)

window.mainloop()