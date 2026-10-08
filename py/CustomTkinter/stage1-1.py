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

# Exercise 4: Frame within frame
"""header = ctk.CTkFrame(window)
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
"""

# Exercise 5: Little DevBoard
header = ctk.CTkFrame(window)
header.pack(fill="x", pady="15", padx="10")
l_h = ctk.CTkLabel(header, text="DevBoard")
l_h.pack(pady="10")

content = ctk.CTkFrame(window)
content.pack(padx=20, pady=(20, 10))

def read_print(a, b):
    a = a.get()
    b = b.get()
    print(f"Key: [{a}]\nShort: [{b}]")

key = ctk.CTkLabel(content, text="Key:")
input_key = ctk.CTkEntry(content)
short = ctk.CTkLabel(content, text="Short:")
input_short = ctk.CTkEntry(content)
confirm = ctk.CTkButton(window, text="Confirm", command=lambda: read_print(input_key, input_short))

key.grid(row=0, column=0, padx=(40, 5), pady=(40, 5))
input_key.grid(row=0, column=1, padx=(5, 40), pady=(40, 5))
short.grid(row=1, column=0, padx=(40, 5), pady=(5, 40))
input_short.grid(row=1, column=1, padx=(5, 40), pady=(5, 40))
confirm.pack() # i left it out the Content for keep it aligned in center

window.mainloop()