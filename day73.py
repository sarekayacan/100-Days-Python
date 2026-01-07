#Handwriting Digit Recognition
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Input
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageOps

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

model = Sequential([
    Input(shape=(28,28,1)),
    Conv2D(32, (3,3), activation='relu'),
    MaxPooling2D((2,2)),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D((2,2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test Accuracy: {test_acc*100:.2f}%")

def load_and_predict():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    try:
        img = Image.open(file_path).convert('L')   
        img = ImageOps.invert(img)                  
        img = img.resize((28,28))               
        img_array = np.array(img).astype('float32') / 255.0
        img_array = img_array.reshape(1,28,28,1)   
        pred = np.argmax(model.predict(img_array))
        messagebox.showinfo("Tahmin", f"Bu rakam: {pred}")
    except Exception as e:
        messagebox.showerror("Hata", str(e))

root = tk.Tk()
root.title("El Yazısı Rakam Tanıma")
tk.Button(root, text="Rakam Görseli Yükle", command=load_and_predict).pack(padx=20, pady=20)
root.mainloop()
