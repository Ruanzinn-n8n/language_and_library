import customtkinter as ctk

window = ctk.CTk()
window.geometry("500x300")

label = ctk.CTkLabel(window, text="Olá DevBoard!")
label.pack()

window.mainloop()