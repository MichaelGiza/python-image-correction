from PIL import Image, ImageEnhance, ImageFilter
import os
import tkinter as tk
from tkinter import filedialog

def process_images(folder_path):
    output_path = "./AfterImgs"

    for filename in os.listdir(folder_path):
        img = Image.open(f"{folder_path}/{filename}")

        # Image processing without rotation
        edit = img.filter(ImageFilter.SHARPEN).convert('L')
        
        # Adjusting contrast
        factor = 1.5
        enhancer = ImageEnhance.Contrast(edit)
        edit = enhancer.enhance(factor)

        # Save the processed image
        clean_name = os.path.splitext(filename)[0]
        edit.save(f'{output_path}/{clean_name}_edited.jpg')

    # Information about the completion of processing
    result_label.config(text="Images processed!")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    folder_path_var.set(folder_selected)

def start_processing():
    folder_path = folder_path_var.get()
    if folder_path:
        process_images(folder_path)

# Creating the main window
root = tk.Tk()
root.title("Image Processor")

# Button to choose a folder
browse_button = tk.Button(root, text="Choose folder", command=browse_folder)
browse_button.pack(pady=10)

# Variable holding the path to the folder
folder_path_var = tk.StringVar()
folder_path_entry = tk.Entry(root, textvariable=folder_path_var, state="readonly", width=40)
folder_path_entry.pack(pady=10)

# Button to process images
process_button = tk.Button(root, text="Process images", command=start_processing)
process_button.pack(pady=10)

# Label to display information
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
