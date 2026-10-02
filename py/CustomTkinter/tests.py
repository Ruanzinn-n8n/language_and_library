import customtkinter as ctk

window = ctk.CTk()
window.geometry("500x300")

frame = ctk.CTkFrame(window, width=300, height=200)
frame.place(x=100, y=50)

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

window.mainloop()