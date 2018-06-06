"""Runs the apodapi.py, curiositypic.py, astrosapi.py, isslocation.py, and
spacexlaunch.py scripts.  Builds the GUI for the saved photos and information."""

import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

import apodapi
import astrosapi
import curiosityphotoapi
import isslocation
import spacexlaunch

print("Getting APOD")
apoddata = apodapi.get_apod()
print("Getting Curiosity photo")
cam, sol = curiosityphotoapi.main()
print("Getting the people in space")
astros_number, astronauts = astrosapi.astros()
print("Getting the ISS data")
iss_data = isslocation.iss_data()
print("Getting SpaceX data")
spacex_data = spacexlaunch.next_launch()


def image_plotter(picname, width=500, max_height=500):
    """Uses the height/width ratio to resize the image"""
    pil_image = Image.open(picname)
    height = image_ratio(pil_image, width)
    if height > max_height:
        divider = float(height / max_height)
        width = int(width / divider)
        height = int(height / divider)
    pil_image = pil_image.resize((width, height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(pil_image), width, height


def image_ratio(pil_image, width):
    """Determines the height and width ratio of the picture"""
    npimage = np.asarray(pil_image, dtype=np.uint8)
    img_h = npimage.shape[0]
    img_w = npimage.shape[1]
    height = (img_h / img_w) * width
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
            if string[string_index] == " ":
                line_string = string[:string_index]
                line_list.append(line_string)
                # Removes the selected line from the string
                string = string[string_index + 1 :]
                space_checker = False
            else:
                string_index += 1
    # Adds the remainder of the string as the last line
    line_list.append(string)
    return line_list


root = tk.Tk()
root.wm_title("Space Desktop")


root.geometry("1500x700")
canvas = tk.Canvas(root, width=1499, height=699)
cv = tk.Canvas()
cv.pack(side="top", fill="both", expand="yes")


apod_image, apod_width, apod_height = image_plotter("apod.jpg", width=600)
# The top left corner coordinates of the APOD picture
apod_x, apod_y = 20, 35
# Creates the heading and image for the APOD
cv.create_text(
    (2 * apod_x + apod_width) / 2,
    apod_y - 15,
    text="Astronomy Picture of the Day",
    font="Verdana 16 bold",
)
cv.create_image(apod_x, apod_y, image=apod_image, anchor="nw")
# The y position of the first line of the APOD explanation
apod_caption_y = apod_y + apod_height + 12
# Creates a list of substrings from the APOD explanation
lines = text_display(apoddata["explanation"], line_length=90)
# Displays each individual line in lines list
for line in lines:
    cv.create_text(apod_x, apod_caption_y, text=line, font="Verdana 8", anchor="nw")
    # Adjusts y location of subsequent lines
    apod_caption_y += 11

# Creates the image heading for a Curiosity photo
curiosity_image, curiosity_width, curiosity_height = image_plotter(
    "curiositypic.jpg", width=400
)
# Creates the reference points for the top left corner of the Curiosity image
curiosity_x, curiosity_y = 650, 35
cv.create_text(
    (2 * curiosity_x + curiosity_width) / 2,
    curiosity_y - 15,
    text="Curiosity Photo",
    font="Verdana 16 bold",
)
cv.create_image(curiosity_x, curiosity_y, image=curiosity_image, anchor="nw")
cv.create_text(
    (2 * curiosity_x + curiosity_width) / 2,
    curiosity_y + curiosity_height + 15,
    text="Camera: " + cam + " Sol: " + sol,
    font="Verdana 8",
)

# Creates the reference points for the People in Space API data
astros_x = curiosity_x
astros_y = curiosity_y + curiosity_height + 35
# Prints the People in Space header titles
cv.create_text(astros_x, astros_y, text="Name", font="Verdana 12 bold", anchor="nw")
cv.create_text(
    astros_x + 150, astros_y, text="Craft", font="Verdana 12 bold", anchor="nw"
)
# Creates a space between the header and the listings
astros_y += 25
# Prints the names and spacecraft of the individuals in space
for astro in astronauts:
    cv.create_text(
        astros_x, astros_y, text=astro["name"], font="Verdana 10", anchor="nw"
    )
    cv.create_text(
        astros_x + 150, astros_y, text=astro["craft"], font="Verdana 10", anchor="nw"
    )
    astros_y += 15
# The location of the ISS header
iss_x, iss_y = 1100, 15
cv.create_text(iss_x, iss_y, text="ISS Location", font="Verdana 16 bold", anchor="nw")
iss_y += 25
# List of data labels and the dictionary values for ISS data
iss_data_text = [
    "UTC Date: " + str(iss_data["date"]),
    "UTC Time: " + str(iss_data["time"]),
    "Latitude: " + str(iss_data["lat"]),
    "Longitude: " + str(iss_data["long"]),
]
# Displays the ISS data in the issdatatext list
for text in iss_data_text:
    cv.create_text(iss_x, iss_y, text=text, font="Verdana 10", anchor="nw")
    iss_y += 15

# The SpaceX header location
spacex_x, spacex_y = iss_x, iss_y + 35
# Displays the ISS location and date and time
cv.create_text(
    spacex_x, spacex_y, text="Next SpaceX Launch", font="Verdana 16 bold", anchor="nw"
)
spacex_y += 25
# List of data labels and the dictionary values for SpaceX data
spacex_data_text = [
    ["Date", spacex_data["date"]],
    ["Time", spacex_data["time"]],
    ["Site", spacex_data["site"]],
    ["Type", spacex_data["rocket_type"]],
]
# Displays the ISS data in the iss_data_text list
for text in spacex_data_text:
    cv.create_text(spacex_x, spacex_y, text=text[0], font="Verdana 12", anchor="nw")
    spacex_y += 20
    cv.create_text(spacex_x, spacex_y, text=text[1], font="Verdana 10", anchor="nw")
    spacex_y += 15
# Displays payloads separately in case of multiple payloads
cv.create_text(spacex_x, spacex_y, text="Payload(s)", font="Verdana 12", anchor="nw")
spacex_y += 20
for payload in spacex_data["payloads"]:
    cv.create_text(spacex_x, spacex_y, text=payload, font="Verdana 10", anchor="nw")
    spacex_y += 15


root.mainloop()
