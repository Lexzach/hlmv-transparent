import sys
import os
import glob
import tkinter as tk
from PIL import Image, ImageDraw, ImageFont, ImageChops

cropImage = []

for x in glob.glob("./Cropping Folder/*.png"):
    cropImage.append(x)

run = tk.Tk()
var = tk.IntVar()
run.title("Transparent Cropper")
Message = tk.Frame(master=run)
temp = tk.Label(master=Message, text="Press the crop button to crop "+str(len(cropImage))+" images.")
okay = tk.Button(master=Message, text="- CROP -",command=lambda: var.set(1))
temp.grid(row=1, column=0, sticky="w")
okay.grid(row=10, column=0, sticky="s")
Message.grid(row=0, column=0, sticky="w")
temp.wait_variable(var)

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

for x in cropImage:
    im = Image.open(x)
    im = trim(im)
    im.save(x[:-4] + "_cropped.png")