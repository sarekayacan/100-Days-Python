#Object Detection App
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
from tkinter import messagebox

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant",
           "sheep", "sofa", "train", "tvmonitor"]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

net = cv2.dnn.readNetFromCaffe(
    os.path.join(BASE_DIR, "MobileNetSSD_deploy.prototxt"),
    os.path.join(BASE_DIR, "MobileNetSSD_deploy.caffemodel")
)

def detect_objects(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Resim okunamadı. Lütfen JPG veya PNG bir dosya seç.")
   
    (h, w) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(
        cv2.resize(image, (300, 300)),
        0.007843, (300, 300), 127.5
    )

    net.setInput(blob)
    detections = net.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > 0.5:
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (x1, y1, x2, y2) = box.astype("int")

            label = f"{CLASSES[idx]}: {confidence:.2f}"
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(
    image,
    label,
    (x1 + 5, y1 + 20),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.7,
    (0, 255, 0),
    2
)
    return image

def open_image():
    path = filedialog.askopenfilename(
        title="Bir resim seç",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
    )
    if not path:
        return
    try:
        result = detect_objects(path)
    except Exception as e:
        messagebox.showerror("Hata", str(e))
        return

    result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

    img = Image.fromarray(result)
    img = img.resize((600, 400))
    img = ImageTk.PhotoImage(img)

    panel.image = img
    panel.config(image=img)

root = tk.Tk()
root.title("SSD MobileNet Nesne Algılama")

btn = tk.Button(root, text="Resim Seç", command=open_image)
btn.pack(pady=10)

panel = tk.Label(root)
panel.pack()

root.mainloop()
