
import tkinter as tk
from tkinter import messagebox
import datetime

def calculate_bmi(weight, height):

    try:
        bmi = weight / (height ** 2)
        category = classify_bmi(bmi)
        return bmi, category
    except ZeroDivisionError:
        return None, None
    
def classify_bmi(bmi):

    if bmi is None:
        return None
    elif bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesed"
    
def save_bmi_record(weight, height, bmi, category):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    record = f"{timestamp}, {weight}, {height}, {bmi: .2f}, {category}\n"
    with open("bmi_history.txt", "a") as file:
        file.write(record)

def view_bmi_history():

    try:
        with open("bmi_history.txt", "r") as file:
            history = file.readlines()
            if not history:
                messagebox.showinfo("BMI History", "No BMI records found.")
                return
            history_text = "\n".join(history)
            messagebox.showinfo("BMI History", history_text)
    except FileNotFoundError:
        messagebox.showerror("Error", "BMI History not found.")

def calculate_button_clicked():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for capturing weight and height details.")
        return
       
    bmi, category = calculate_bmi(weight, height)
    if bmi is not None:
        result_label.config(text=f"Your BMI is {bmi:.2f} ({category})")
        save_bmi_record(weight, height, bmi, category)

root = tk.Tk()
root.title("BMI Calculator")

weight_label = tk.Label(root, text="Weight (kg):")
weight_entry = tk.Entry(root)
height_label = tk.Label(root, text="Height (m):")
height_entry = tk.Entry(root)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_button_clicked)

view_history_button = tk.Button(root, text="View BMI History", command=view_bmi_history)

result_label = tk.Label(root, text="")

weight_label.grid(row=0, column=0)
weight_entry.grid(row=0, column=1)
height_label.grid(row=1, column=0)
height_entry.grid(row=1, column=1)

calculate_button.grid(row=2, columnspan=2)
view_history_button.grid(row=3, columnspan=2)
result_label.grid(row=4, columnspan=2)

root.mainloop()
        