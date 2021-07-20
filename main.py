import tkinter as tk
from tkinter import filedialog, StringVar, OptionMenu
from PIL import Image, ImageFont, ImageDraw
import matplotlib.pyplot as plt


def upload_image():
    filename = filedialog.askopenfilename()
    image = Image.open(filename)
    watermark_image = image.copy()
    width, height = watermark_image.size
    margin = 200
    draw = ImageDraw.Draw(watermark_image)
    font = ImageFont.truetype("arial.ttf", 50)

    global text_col
    global text_loc

    if text_col.get() == "white":
        text_color = (255, 255, 255)
    else:
        text_color = (0, 0, 0)

    print(width)
    print(height)

    if text_loc.get() == "Top Left":
        watermark_position = (0, 0)
    elif text_loc.get() == "Top Right":
        watermark_position = (width-margin, 0)
    elif text_loc.get() == "Bottom Left":
        watermark_position = (0, height-50)
    else:
        watermark_position = (width-margin, height-50)

    # add a watermark
    draw.text(watermark_position, "Giovanni",
              text_color, font=font)
    plt.subplot(1, 2, 1)
    plt.imshow(watermark_image)
    watermark_image.show()


root = tk.Tk()
upload_button = tk.Button(root, text='Open File', command=upload_image)
upload_button.pack()

text_col = StringVar(root)
text_col.set("white")  # default value

color_dropdown = OptionMenu(root, text_col, "white", "black")
color_dropdown.pack()


text_loc = StringVar(root)
text_loc.set("Top Left")

location_dropdown = OptionMenu(root, text_loc, "Top Left", "Top Right", "Bottom Left", "Bottom Right")
location_dropdown.pack()

root.mainloop()
