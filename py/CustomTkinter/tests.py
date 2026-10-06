import customtkinter as ctk

window = ctk.CTk()
window.geometry("500x300")

frame = ctk.CTkFrame(window)
frame.pack(fill="both", expand="True")

label = ctk.CTkLabel(frame, text="DevBoard")
label.grid(row=0, column=0, sticky="nsew")

window.mainloop()