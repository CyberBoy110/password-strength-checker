

import tkinter as tk
from password_checker import check_password_strength
def evaluate_password():
    password = entry.get()
    result = check_password_strength(password)
    result_label.config(text=f"Strength: {result}")

# Set up window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")

# Widgets
label = tk.Label(root, text="Enter Password:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack()

check_button = tk.Button(root, text="Check Strength", command=evaluate_password, font=("Arial", 12))
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

# Run GUI
root.mainloop()
