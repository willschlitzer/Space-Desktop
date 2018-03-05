import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

import api_config
import apodapi
import astrosapi
import curiosityphotoapi


def image_plotter(picname, width = 500, maxheight = 600):
    pil_image = Image.open(picname)
    height = image_ratio(pil_image, width)
    pil_image = pil_image.resize((height, width), Image.ANTIALIAS)
    return ImageTk.PhotoImage(pil_image)


def image_ratio(pil_image, width):
    npimage = np.asarray(pil_image, dtype=np.uint8)
    img_h = npimage.shape[0]
    img_w = npimage.shape[1]
    print(img_h, img_w)
    height = (img_h/img_w) * width
    return int(round(height, 0))


root= tk.Tk()


root.geometry('1500x700')
canvas= tk.Canvas(root, width= 1499, height= 699)
cv = tk.Canvas()
cv.pack(side='top', fill='both', expand='yes')
apodimage= image_plotter('apod.jpg')
cv.create_image(20, 30, image = apodimage, anchor='nw')
curiosityimage = image_plotter('curiositypic.jpg', width = 200)
cv.create_image(600, 30, image= curiosityimage, anchor='nw')

root.mainloop()
