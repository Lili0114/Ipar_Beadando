import tkinter as tk
import subprocess

def run_single():
    subprocess.run(["python", "object_detection.py"])

def run_multiple():
    subprocess.run(["python", "multiple_object_detection.py"])

root = tk.Tk()
root.title("Indítás")
root.geometry("400x200+600+200")

single_button = tk.Button(root, text="EGY OBJEKTUM", command=run_single)
single_button.pack(fill=tk.X, padx=50, pady=15, anchor='center', expand=True)

multiple_button = tk.Button(root, text="TÖBB OBJEKTUM", command=run_multiple)
multiple_button.pack(fill=tk.X, padx=50, pady=10, anchor='center', expand=True)

root.mainloop()