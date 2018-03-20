"""Runs the apodapi.py, curiositypic.py, astrosapi.py, and isslocation.py
scripts.  Builds the GUI for the saved photos and information."""

import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

import apodapi
import astrosapi
import curiosityphotoapi
import isslocation
import spacexlaunch

print('Getting APOD')
apoddata = apodapi.get_apod()
print('Getting Curiosity photo')
cam, sol = curiosityphotoapi.main()
print('Getting the people in space')
astros_number, astronauts = astrosapi.astros()
print('Getting the ISS data')
issdata = isslocation.iss_data()

def image_plotter(picname, width = 500):
    """Uses the image_ratio to determine the height and width of the photo, and resizes the image"""
    pil_image = Image.open(picname)
    height = image_ratio(pil_image, width)
    pil_image = pil_image.resize((width, height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(pil_image)


def image_ratio(pil_image, width):
    """Determines the height and width ratio of the picture"""
    npimage = np.asarray(pil_image, dtype=np.uint8)
    img_h = npimage.shape[0]
    img_w = npimage.shape[1]
    height = (img_h/img_w) * width
    return int(round(height, 0))

def text_display(string, line_length=45):
    """Takes a string and returns a list of substrings"""
    line_list = []
    #iterations = int(round(len(string)/line_length, 0))
    #print(iterations)
    print(len(string))
    while len(string) > line_length:
        print(string)
        string_index = line_length - 5
        space_checker = True
        while space_checker == True:
            if string[string_index] == ' ':
                line_string = string[:string_index]
                line_list.append(line_string)
                string = string[string_index+1:]
                space_checker = False
            else:
                string_index += 1
        print(line_list)
    line_list.append(string)
    return line_list

root = tk.Tk()


root.geometry('1500x700')
canvas = tk.Canvas(root, width= 1499, height= 699)
cv = tk.Canvas()
cv.pack(side='top', fill='both', expand='yes')

# Creates the heading and image for the APOD
apodimage = image_plotter('apod.jpg', width = 600)
cv.create_text(175,7, text='Astronomy Picture of the Day', font="Verdana 16 bold", anchor='nw')
cv.create_image(20, 35, image = apodimage, anchor='nw')

# Creates the image heading for a Curiosity photo
curiosityimage = image_plotter('curiositypic.jpg', width = 400)
cv.create_text(800,15, text='Curiosity Photo', anchor = 'nw')
cv.create_image(650, 35, image= curiosityimage, anchor='nw')

# Creates the reference points for the People in Space API data
x1 = 650
x2 = x1 + 150
y1 = 450
y2 = y1 + 10

# Prints the People in Space header titles
cv.create_text(x1 + 5, y2 + 5, text='Name', anchor = 'nw')
cv.create_text(x2 + 5, y2 + 5, text='Craft', anchor = 'nw')
# Prints the names and spacecraft of the individuals in space
for astro in astronauts:
    y2 = y2 + 25
    astroname = astro['name']
    astrocraft = astro['craft']
    cv.create_text(x1 + 5, y2, text=astroname, anchor = 'nw')
    cv.create_text(x2 + 5, y2, text=astrocraft, anchor = 'nw')

# The ISS location data and the current time of the request
issdata, date_time = isslocation.iss_data()
iss_lat, iss_long = issdata['iss_position']['latitude'], issdata['iss_position']['longitude']
# Displays the ISS location and date and time
cv.create_text(1100, 15, text='ISS Location', anchor='nw')
cv.create_text(1100, 30, text='Date: ' + str(date_time), anchor='nw')
cv.create_text(1100, 45, text='Latitude: ' + str(iss_lat), anchor='nw')
cv.create_text(1100, 60, text='Longitude: ' + str(iss_long), anchor='nw')



root.mainloop()
