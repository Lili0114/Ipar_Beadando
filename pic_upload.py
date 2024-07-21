import tkinter as tk
from tkinter import filedialog

with open('coco.name.two', 'r') as f:
    names = f.read().splitlines()

def on_select(event):    
    print("Selected:", event.widget.get(event.widget.curselection()))
    filePath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png")])
    print("Selected file:", filePath)

root = tk.Tk()
root.title("Objektum választása")
root.geometry("400x450+600+200")

caption = tk.Label(root, text="Válassz egy objektumot \na felsoroltak közül!\n", font=("Arial", 20))
caption.pack()

# Frame a listbox és scrollbarnak
frame = tk.Frame(root)
frame.pack()

# Scrollbar
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Lista
listbox = tk.Listbox(frame, width=40, height=15, yscrollcommand=scrollbar.set)
listbox.bind('<<ListboxSelect>>', on_select)

for name in names:
    listbox.insert(tk.END, name)

listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar.config(command=listbox.yview)

root.mainloop()