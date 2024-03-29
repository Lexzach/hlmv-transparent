import sys
import os
import glob
import tkinter as tk
from PIL import Image, ImageDraw, ImageFont, ImageChops
from PIL.PngImagePlugin import PngImageFile, PngInfo

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
    im = im.crop((0, 10, im.size[0], im.size[1]))
    bg = Image.new(im.mode, (im.size[0], im.size[1]), im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

for x in cropImage:
    im = Image.open(x)
    im = trim(im)
    meta = PngInfo()
    meta.add_text("Made using", f"HLMV Transparent Cropper - https://wiki.teamfortress.com/wiki/User:Lexzach")
    im.save(x[:-4] + "_cropped.png", pnginfo=meta)