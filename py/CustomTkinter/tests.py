import customtkinter as ctk

window = ctk.CTk()
window.geometry("500x300")

frame = ctk.CTkFrame(window, width=300, height=200)
frame.place(x=100, y=50)

def read_write(a, b):
    a = a.get()
    b = b.get()
    print(f"Nome do usuário: {a}\nIdade: {b}")

name = ctk.CTkLabel(frame, text="Name:  ")
name.place(x=50, y=50)

inputname = ctk.CTkEntry(frame)
inputname.place(x=110, y=50)

age = ctk.CTkLabel(frame, text="Age:  ")
age.place(x=63, y=80)

inputage = ctk.CTkEntry(frame)
inputage.place(x=110, y=80)

confirm = ctk.CTkButton(frame, text="Confirm", command=lambda:read_write(inputname, inputage))
confirm.place(x=80, y=130)

window.mainloop()