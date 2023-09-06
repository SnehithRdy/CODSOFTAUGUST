#Password_Genrator GUI
import tkinter as tk
from tkinter import font as tkfont
import random
import string

def generate_password():
    length = int(length_entry.get())
    complexity = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(complexity) for i in range(length))
    bold_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
    display_label.config(text=f"Generated Password: {password}",font=bold_font)

#Main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("300x150")
root.configure(bg="lightblue")
#Labels and entry for password length
length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()
#Button to generate the password
generate = tk.Button(root, text="Generate Password", command=generate_password)
generate.pack()
#Display the generated password
display_label = tk.Label(root, text="")
display_label.pack()
display_label.configure(bg="lightblue")

root.mainloop()
