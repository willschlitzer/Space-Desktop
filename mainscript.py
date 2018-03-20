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
print('Getting SpaceX data')
spacexdata = spacexlaunch.next_launch()


def image_plotter(picname, width = 500):
    """Uses the height/width ratio to resize the image"""
    pil_image = Image.open(picname)
    height = image_ratio(pil_image, width)
    pil_image = pil_image.resize((width, height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(pil_image), width, height


def image_ratio(pil_image, width):
    """Determines the height and width ratio of the picture"""
    npimage = np.asarray(pil_image, dtype=np.uint8)
    img_h = npimage.shape[0]
    img_w = npimage.shape[1]
    height = (img_h/img_w) * width
    return int(round(height, 0))

def text_display(string, line_length=45):
    """Takes a string and returns a list of substrings"""
    # Empty list that will contain the lines of the string
    line_list = []
    while len(string) > line_length:
        # Looks for a space in the string starting 5 characters from the line length
        string_index = line_length - 5
        space_checker = True
        while space_checker == True:
            if string[string_index] == ' ':
                line_string = string[:string_index]
                line_list.append(line_string)
                # Removes the selected line from the string
                string = string[string_index+1:]
                space_checker = False
            else:
                string_index += 1
    # Adds the remainder of the string as the last line
    line_list.append(string)
    return line_list

root = tk.Tk()


root.geometry('1500x700')
canvas = tk.Canvas(root, width= 1499, height= 699)
cv = tk.Canvas()
cv.pack(side='top', fill='both', expand='yes')


apodimage, apodwidth, apodheight = \
    image_plotter('apod.jpg', width= 500)
# The top left corner coordinates of the APOD picture
apodx, apody = 20, 35
# Creates the heading and image for the APOD
cv.create_text((2*apodx+apodwidth)/2,apody-15,
               text='Astronomy Picture of the Day', font="Verdana 16 bold")
cv.create_image(apodx, apody, image = apodimage, anchor='nw')
# The y position of the first line of the APOD explanation
apodexplanationy = apody + apodheight + 12
# Creates a list of substrings from the APOD explanation
lines = text_display(apoddata['explanation'], line_length = 90)
for line in lines:
    cv.create_text(apodx, apodexplanationy,
                   text=line, font = "Verdana 8", anchor='nw')
    apodexplanationy += 11
# Creates the image heading for a Curiosity photo
curiosityimage, curiositywidth, curiosityheight = \
    image_plotter('curiositypic.jpg', width = 400)
# Creates the reference points for the top left corner of the Curiosity image
curiosityx, curiosityy = 650, 35
cv.create_text((2*curiosityx+curiositywidth)/2,curiosityy-15,
               text='Curiosity Photo', font = "Verdana 16 bold")
cv.create_image(curiosityx, curiosityy,
                image= curiosityimage, anchor='nw')

# Creates the reference points for the People in Space API data
astrosx = curiosityx
astrosy = curiosityy + curiosityheight + 25
# Prints the People in Space header titles
cv.create_text(astrosx, astrosy, text='Name',
               font = "Verdana 12 bold", anchor ='nw')
cv.create_text(astrosx + 150, astrosy, text='Craft',
               font = "Verdana 12 bold", anchor ='nw')
# Creates a space between the header and the listings
astrosy += 25
# Prints the names and spacecraft of the individuals in space
for astro in astronauts:
    cv.create_text(astrosx, astrosy, text=astro['name'], font="Verdana 10", anchor ='nw')
    cv.create_text(astrosx + 150, astrosy, text=astro['craft'], font="Verdana 10", anchor ='nw')
    astrosy += 15
# The location of the ISS header
issx, issy = 1100, 15
cv.create_text(issx, issy, text='ISS Location', font="Verdana 16 bold", anchor='nw')
issy += 25
# List of data labels and the dictionary values for ISS data
issdatatext = ['UTC Date: ' + str(issdata['date']),
               'UTC Time: ' + str(issdata['time']),
               'Latitude: ' + str(issdata['lat']),
               'Longitude: ' + str(issdata['long'])]
# Displays the ISS data in the issdatatext list
for text in issdatatext:
    cv.create_text(issx, issy, text=text, font="Verdana 10", anchor='nw')
    issy += 15

# The SpaceX header location
spacexx, spacexy = issx, issy+35
# Displays the ISS location and date and time
cv.create_text(spacexx, spacexy, text='Next SpaceX Launch', font="Verdana 16 bold", anchor='nw')
spacexy += 25
# List of data labels and the dictionary values for SpaceX data
spacexdatatext = [['Date', spacexdata['date']],
                  ['Time', spacexdata['time']],
                  ['Site', spacexdata['site']],
                  ['Type', spacexdata['rocket_type']]]
# Displays the ISS data in the issdatatext list
for text in spacexdatatext:
    cv.create_text(spacexx, spacexy, text=text[0], font="Verdana 12", anchor='nw')
    spacexy += 20
    cv.create_text(spacexx, spacexy, text=text[1], font="Verdana 10", anchor='nw')
    spacexy += 15
cv.create_text(spacexx, spacexy, text='Payload(s)', font="Verdana 12", anchor='nw')
spacexy += 20
for payload in spacexdata['payloads']:
    cv.create_text(spacexx, spacexy, text=payload, font="Verdana 10", anchor='nw')
    spacexy += 15


root.mainloop()
