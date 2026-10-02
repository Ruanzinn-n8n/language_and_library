import customtkinter as ctk

app = ctk.CTk()
app.geometry("500x300")

input = ctk.CTkEntry(app)
input.pack()

text = input.get()

input.delete(0, "end")
print(text)

app.mainloop()