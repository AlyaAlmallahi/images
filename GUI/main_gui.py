import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import subprocess
import os

# Global variables
selected_image_path = None
selected_operation = None

# Function to upload an image
def upload_image():
    global selected_image_path
    selected_image_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
    )
    if selected_image_path:
        image_label.config(text=f"Selected Image: {os.path.basename(selected_image_path)}")
    else:
        image_label.config(text="No image selected")

# Function to execute a Python script
def execute_script():
    global selected_image_path, selected_operation
    if not selected_image_path:
        messagebox.showerror("Error", "Please upload an image first!")
        return
    if not selected_operation:
        messagebox.showerror("Error", "Please select an operation!")
        return

    try:
        # Pass the selected image path as an argument to the script
        
        subprocess.run(["python3", selected_operation, "--image", selected_image_path], check=True)
        messagebox.showinfo("Success", f"Executed: {os.path.basename(selected_operation)}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to execute: {selected_operation}\n{e}")

# Function to update the selected operation
def update_operation(operation_path):
    global selected_operation
    selected_operation = operation_path
    operation_label.config(text=f"Selected Operation: {os.path.basename(operation_path)}")

# Create the main window
root = tk.Tk()
root.title("Image Processing & Clustering GUI")
root.geometry("500x600")
root.configure(bg="#f0f0f0")

# Add a title label
title_label = tk.Label(root, text="Image Processing & Clustering", font=("Arial", 18, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Add an image upload button
upload_button = tk.Button(root, text="Upload Image", command=upload_image, font=("Arial", 12), bg="#4CAF50", fg="white")
upload_button.pack(pady=10)

# Label to display selected image
image_label = tk.Label(root, text="No image selected", font=("Arial", 10), bg="#f0f0f0")
image_label.pack(pady=5)

# Add a dropdown menu for operations
operations = {
    "K-Means Clustering": "/Users/aliasuleiman/Downloads/Project/Model Selection/K-Means.py",
    "Sharpening": "/Users/aliasuleiman/Downloads/Project/Image Preprocessing/Sharpening.py",
    "Resizing & Normalization": "/Users/aliasuleiman/Downloads/Project/Image Preprocessing/Resizing & Normalization.py",
    "Noise Reduction": "/Users/aliasuleiman/Downloads/Project/Image Preprocessing/Noise Reduction.py",
    "Edge Enhancement": "/Users/aliasuleiman/Downloads/Project/Image Preprocessing/Edge Enhancement.py",
    "Contrast Adjustment": "/Users/aliasuleiman/Downloads/Project/Image Preprocessing/Contrast Adjustment.py",
    "Color Space Conversion": "/Users/aliasuleiman/Downloads/Project/Image Preprocessing/Color Space Conversion.py",
    "Binarization": "/Users/aliasuleiman/Downloads/Project/Image Preprocessing/Binarization.py",
}

operation_label = tk.Label(root, text="No operation selected", font=("Arial", 10), bg="#f0f0f0")
operation_label.pack(pady=5)

operation_menu = ttk.Combobox(root, values=list(operations.keys()), font=("Arial", 12))
operation_menu.set("Select an Operation")
operation_menu.pack(pady=10)

def on_operation_select(event):
    selected_key = operation_menu.get()
    if selected_key in operations:
        update_operation(operations[selected_key])

operation_menu.bind("<<ComboboxSelected>>", on_operation_select)

# Add an execute button
execute_button = tk.Button(root, text="Apply Operation", command=execute_script, font=("Arial", 12), bg="#2196F3", fg="white")
execute_button.pack(pady=20)

# Run the GUI loop
root.mainloop()
