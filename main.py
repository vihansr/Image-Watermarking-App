from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import filedialog

# Watermark Command
def add_watermark():
    root.withdraw()
    filepath = filedialog.askopenfilename()
    img = Image.open(filepath).convert("RGBA")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 20)
    text = entry.get()

    # Get image dimensions
    img_width, img_height = img.size
    x_min, y_min, x_max, y_max = font.getbbox(text)
    text_width = x_max - x_min
    text_height = y_max - y_min

    # Define spacing for the watermark grid
    x_spacing = text_width + 50
    y_spacing = text_height + 50

    # Draw watermarks in a grid pattern
    for x in range(0, img_width, x_spacing):
        for y in range(0, img_height, y_spacing):
            draw.text((x, y), text, font=font, fill=(255, 255, 255, 128))  # Semi-transparent white

    img.show()


# GUI
root = tk.Tk()
root.title("Image Watermarking App")
root.geometry("400x300")

title_label = tk.Label(root, text="Image Watermarking", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), width=30, bd=2, relief=tk.GROOVE)
entry.pack(pady=10)

submit_btn = tk.Button(root, text="Convert", font=("Arial", 12, "bold"), padx=10, pady=5, command=add_watermark)
submit_btn.pack(pady=10)

root.mainloop()
