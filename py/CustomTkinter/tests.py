import customtkinter as ctk

window = ctk.CTk()
window.geometry("500x300")

header = ctk.CTkFrame(window)
header.pack(fill="x", pady="10", padx="5")
l_head = ctk.CTkLabel(header, text="Header")
l_head.pack()

content = ctk.CTkFrame(window)
content.pack(fill="both", padx="5")

right = ctk.CTkFrame(content)
right.grid(row=0, column=1, padx="3", pady="20")
l_rgh = ctk.CTkLabel(right, text="Right")
l_rgh.pack(pady="150", padx="150")

left = ctk.CTkFrame(content)
left.grid(row=0, column=0, padx="18", pady="20")
l_lft = ctk.CTkLabel(left, text="Left")
l_lft.pack(pady="150", padx="150")

window.mainloop()