import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

import api_config
import apodapi
import astrosapi
import curiosityphotoapi

def image_plotter(picname, width = 500):
    pilImage = Image.open(picname)
    height = image_ratio(pilImage, width)
    pilImage = pilImage.resize((height, width), Image.ANTIALIAS)
    print(height, width)
    return ImageTk.PhotoImage(pilImage)

def image_ratio(pilImage, width):
    npimage = np.asarray(pilImage, dtype=np.uint8)
    img_h = npimage.shape[0]
    img_w = npimage.shape[1]
    print(img_h, img_w)
    height = (img_h/img_w) * width
    return (int(round(height,0)))

root= tk.Tk()
root.geometry('10000x10000')
canvas = tk.Canvas(root, width=9999, height = 9999)
cv = tk.Canvas()
cv.pack(side='top', fill='both', expand='yes') 
apodimage = image_plotter('apod.jpg')
cv.create_image(20, 30, image = apodimage, anchor='nw')
curiosityimage = image_plotter('curiositypic.jpg', width = 200)
cv.create_image(600, 30, image = curiosityimage, anchor='nw')

root.mainloop()
