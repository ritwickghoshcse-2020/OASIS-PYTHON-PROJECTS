
import random
import string
import pyperclip
from tkinter import*

def generate_password():
    password_length = pass_len.get()

    # Define character sets

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine character sets based on user preferences

    selected_characters = ""
    
    if use_lowercase.get():
        selected_characters += lowercase_letters
    if use_uppercase.get():
        selected_characters += uppercase_letters
    if use_digits.get():
        selected_characters += digits
    if use_symbols.get():
        selected_characters += symbols

    if not selected_characters:
        print("Please select at least one character type.")
        return
    
    password = ''.join(random.choice(selected_characters) for _ in range(password_length))
    pyperclip.copy(password)
    print(f"Generated password: {password}")

root = Tk()
root.geometry("400x400")
root.title("Random Password Generator")

pass_head = Label(root, text='Password Length', font='arial 12 bold').pack(pady=10)
pass_len = IntVar()
length_spinbox = Spinbox(root, from_=4, to_=32, textvariable=pass_len, width=24,font='arial 16').pack()

use_lowercase = BooleanVar()
use_uppercase = BooleanVar()
use_digits = BooleanVar()
use_symbols = BooleanVar()

lowercase_check = Checkbutton(root, text="Lowercase", variable=use_lowercase).pack()
uppercase_check = Checkbutton(root, text="Uppercase", variable=use_uppercase).pack()
digits_check = Checkbutton(root, text="Digits", variable=use_digits).pack()
symbols_check = Checkbutton(root, text="Symbols", variable=use_symbols).pack()

generate_button = Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

def copy_to_clipboard():
    password = pyperclip.paste()
    pyperclip.copy(password)
    print("Password copied to clipboard!")

copy_button = Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack()

root.mainloop()