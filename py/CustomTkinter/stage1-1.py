import customtkinter as ctk

window = ctk.CTk()
window.geometry("500x300")

# Exercise 1: Header + content
"""frame1 = ctk.CTkFrame(window)
frame2 = ctk.CTkFrame(window)
frame1.pack(fill="x", pady="5")
frame2.pack(fill="both", expand="True", pady="5")

header = ctk.CTkLabel(frame1, text="DevBoard")
header.pack()

content = ctk.CTkLabel(frame2, text="Hello DevBoard!")
content.pack(pady="150")
"""

# Exercise 2: Fill + Expand
"""frame = ctk.CTkFrame(window)
frame.pack(fill="both", expand="True")

label = ctk.CTkLabel(frame, text="Test")
label.pack()
"""

# Exercise 3: Form
"""cont = ctk.CTkFrame(window)
cont.grid(row=0, column=0, pady="100", padx="220")

key = ctk.CTkLabel(cont, text="Key:")
key.grid(row=0, column=0, pady="5", padx="10", sticky="e")
i_key = ctk.CTkEntry(cont)
i_key.grid(row=0, column=1, pady="5", padx="10")

short = ctk.CTkLabel(cont, text="Shortcut:")
short.grid(row=1, column=0, pady="5", padx="10", sticky="e")
i_short = ctk.CTkEntry(cont)
i_short.grid(row=1, column=1, pady="5", padx="10")

desc = ctk.CTkLabel(cont, text="Description:")
desc.grid(row=2, column=0, pady="5", padx="10", sticky="e")
i_desc = ctk.CTkEntry(cont)
i_desc.grid(row=2, column=1, pady="5", padx="10")

confirm = ctk.CTkButton(window, text="Confirm")
confirm.grid(row=1, column=0)
# all is bad, but ok LOL
"""

# Exercise 4



window.mainloop()