"""Runs the apodapi.py, curiositypic.py, astrosapi.py, and isslocation.py
scripts.  Builds the GUI for the saved photos and information."""

import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

import apodapi
import astrosapi
import curiosityphotoapi
import isslocation

apoddata = apodapi.get_apod()
cam, sol = curiosityphotoapi.main()
astros_number, astronauts = astrosapi.astros()
issdata = isslocation.iss_data()

def create_table(instance, count, data, top_left_coord_x, top_left_coord_y, left_column_title = 'Name', right_column_title = 'Craft',):

    print(data)
    return cv

def image_plotter(picname, width = 500, maxheight =  600):
    pil_image = Image.open(picname)
    height = image_ratio(pil_image, width)
    pil_image = pil_image.resize((height, width), Image.ANTIALIAS)
    return ImageTk.PhotoImage(pil_image)


def image_ratio(pil_image, width):
    npimage = np.asarray(pil_image, dtype=np.uint8)
    img_h = npimage.shape[0]
    img_w = npimage.shape[1]
    height = (img_h/img_w) * width
    return int(round(height, 0))


root = tk.Tk()


root.geometry('1500x700')
canvas = tk.Canvas(root, width= 1499, height= 699)
cv = tk.Canvas()
cv.pack(side='top', fill='both', expand='yes')
apodimage = image_plotter('apod.jpg', width = 600)
cv.create_text(200,15, text='Astronomy Picture of the Day')
cv.create_image(20, 30, image = apodimage, anchor='nw')
curiosityimage = image_plotter('curiositypic.jpg', width = 400)
cv.create_text(850,15, text='Curiosity Photo')
cv.create_image(650, 30, image= curiosityimage, anchor='nw')
x1 = 740
x2 = x1 + 100
x3 = x2 + 60
y1 = 500
y2 = y1 + 5
cv.create_text(x1 + 5, y2 + 5, text='Name')
cv.create_text(x2 + 5, y2 + 5, text='Craft')
for key in astronauts:
    print(key)
    y2 = + 10
    astroname = key['name']
    astrocraft = key['craft']
    cv.create_text(x1 + 5, y2, text=astroname)
    cv.create_text(x1 + 5, y2, text=astrocraft)

root.mainloop()
