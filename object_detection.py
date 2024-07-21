import numpy as np
import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

modellnames = 'objectdataset.data' 
modell = 'pretrained.modell'

min_confidence = 0.2

selected_filePath = None
selected_object = None
classes = []
with open('coco.name.two', 'r') as f:
    classes = f.read().splitlines()

def on_select(event):
    global selected_filePath, selected_object
    selected_object = event.widget.get(event.widget.curselection())
    selected_filePath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png")])
    if selected_filePath != '' and selected_object is not None:
        root.quit()
        analysis(selected_filePath, selected_object)

def show_result(message):
    messageWindow = tk.Tk()
    messageWindow.title("Eredmény")
    messageWindow.geometry("400x200+600+200")

    message_label = tk.Label(messageWindow, text=message, font=("Arial", 14))
    message_label.pack()
    ok_button = tk.Button(messageWindow, text="OK", command=messageWindow.destroy)
    ok_button.pack()
    messageWindow.mainloop()

def analysis(filePath, objectName):
    np.random.seed(543210)
    colors = np.random.uniform(0, 255, size = (len(classes), 3))

    net = cv2.dnn.readNetFromCaffe(modellnames, modell)

    image = cv2.imread(filePath)
    height, width = image.shape[0], image.shape[1]
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007, (300, 300), 130)

    net.setInput(blob)
    detected_objects = net.forward()

    detected_objects_names = []

    for i in range(detected_objects.shape[2]):
            
        confidence = detected_objects[0][0][i][1] 

        if confidence > min_confidence:

            class_index = int(detected_objects[0, 0, i, 1])
            detected_objects_names.append(classes[class_index])

            upper_left_x = int(detected_objects[0, 0, i, 3] * width)
            upper_left_y = int(detected_objects[0, 0, i, 4] * height)
            lower_right_x = int(detected_objects[0, 0, i, 5] * width)
            lower_right_y = int(detected_objects[0, 0, i, 6] * height)

            prediction_text = f"{classes[class_index]}: {confidence:.2f}%"
            cv2.rectangle(image, (upper_left_x, upper_left_y), 
                            (lower_right_x, lower_right_y), 
                            colors[class_index], 2)
            cv2.putText(image, prediction_text, (upper_left_x, 
                            upper_left_y - 15 if upper_left_y > 30 else upper_left_y + 15), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, 
                            colors[class_index], 2)
            
    cv2.imshow('Megjelenites', image)            

    if objectName in detected_objects_names:
        show_result("\nA kiválasztott objektum\nszerepel a képen!\n")
    else:
        show_result("\nA kiválasztott objektum\nnem szerepel a képen!\n")

    cv2.waitKey(0)

# Ablak testreszabása
root = tk.Tk()
root.title("Objektum választása")
root.geometry("400x450+600+200")

caption = tk.Label(root, text="\nVálassz egy objektumot \na felsoroltak közül!\n", font=("Arial", 20))
caption.pack()

frame = tk.Frame(root)
frame.pack()

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame, width=40, height=15, yscrollcommand=scrollbar.set)
listbox.bind('<<ListboxSelect>>', on_select)

for c in classes:
    listbox.insert(tk.END, c)

listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar.config(command=listbox.yview)

root.mainloop()

#if selected_filePath != '' and selected_object is not None:
#    analysis(selected_filePath, selected_object)

