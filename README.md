# HLMV Transparent
This program takes a white background and black background from HLMV and makes a pure transparent image without jagged edges or white edges.

# Dependencies:

Python 3.8.6
-OpenCV `pip install opencv-python`
-Pillow `pip install pillow`
-Glob `pip install glob3`

# How to use:

1. Take two screenshots in HLMV, one with the white background color and the other with the black background color. [THESE SCREENSHOTS MUST BE THE EXACT SAME SIZE, I WOULD RECOMMEND USING WINDOWED SCREENSHOT MODE]

2. Name the screenshot with the white background as `w0.png` and the black background `b0.png`. If you want to do multiple images at the same time, continue to name the images as mentioned above, but change the number from 0 to 1 then to 2, and so on.
As an example, if I wanted to do 2 white images and 2 black images, I would do the following:
`w0.png`
`b0.png`
`w1.png`
`b1.png`
...and when running the program I would type in "2" pairs when prompted.

3. Put those screenshots in the same folder as the program.

4. Run the program.

# Config.txt
-`autoCrop` - Automatically crops the transparent image down to its smallest possible size while keeping all aspects of the image intact.
-`deleteTempFiles` - Automatically clean up temporary files that are generated during operation.

# Like this program?
Do you like this program? If so I would really appreciate it if you would stop by and post something to my talk page on the Team Fortress 2 Wikipedia!

```wiki.teamfortress.com/wiki/User_talk:Lexzach```