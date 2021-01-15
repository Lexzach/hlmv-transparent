Version 1.3

# HLMV Transparent
This is a program specifically designed for the Team Fortress 2 Wiki. It allows perfect transparent images to be easily and automatically created at the push of a button using the out of the box Half-Life Model Viewer program.

# Dependencies:

- Python 3.8.6 `www.python.org/downloads/release/python-386/`
- OpenCV `pip install opencv-python`
- Pillow `pip install pillow`
- Pyautogui `pip install PyAutoGUI`
- Keyboard `pip install keyboard`

Alternatively, you can run the command `pip install -r requirements.txt` to automatically install the dependencies.

# How to install:

- Download Python 3.8.6 from `www.python.org/downloads/release/python-386/`
- Extract ZIP download to your prefered destination.
- Open the `Command prompt`.
- Navigate to the folder that you extracted the program to.
- Click at the top of the Windows Explorer that shows the path, it should look something like `This PC > Downloads > hlmv-transparent-main`, once clicked, the text should turn blue.
- Copy the text and return to the Command prompt.
- Type in `cd` plus a space, and then right click the Command prompt to paste the text.
- Type in `pip install -r requirements.txt`. If this displays an error saying that `pip is not an identified command`, please refer to [this](https://appuals.com/fix-pip-is-not-recognized-as-an-internal-or-external-command/) guide.
- Now your program should be setup, close the command prompt and return to the file explorer.
- Double-click `hlmv-transparent.py` and have fun!

# How to use in manual mode:

1. Take two screenshots in HLMV, one with the white background color and the other with the black background color. Use window capture, as these screenshots **must** be the same size.

2. Name the screenshot with the white background as `w0.png` and the black background `b0.png`. If you want to do multiple images at the same time, continue to name the images as mentioned above, but change the number from 0 to 1 then to 2, and so on.
As an example, if I wanted to do 2 white images and 2 black images, I would do the following:
`w0.png`
`b0.png`
`w1.png`
`b1.png`
...and when running the program I would type in `2` pairs when prompted.

3. Put those screenshots in the **same folder** as the program.

4. Run the program.

# How to use in automatic mode:

**Make sure you change `autoScreenshot` to `true` inside `config.txt`**

1. Run the program.

2. Return to HLMV and press `S` to take a screenshot. (This will move your mouse around)

3. Press the `S` key to take as many screenshots as you wish.

4. Press `P` to finish and start rendering

# Config.txt
- `autoCrop` - Automatically crops the transparent image down to its smallest possible size while keeping all aspects of the image intact.
- `deleteTempFiles` - Automatically clean up temporary files that are generated during operation.
- `autoScreenshot` - Assuming you have a 1920x1080 monitor, and HLMV is maximized (press the square on Windows), the program will automatically move your mouse around to take a screenshot far faster than a human could, after taking the amount of screenshots that the user wants to take, the program will then automatically render them. **REMEMBER: THIS SETTING WILL CONTROL YOUR MOUSE, I AM NOT RESPONSIBLE FOR ANY DAMAGES THAT COULD BE CAUSED BY THIS!!! YOU HAVE BEEN WARNED!**
- `screenshotSizes` - Adjust the size of the screenshot area. This is already coordinated for a 1920x1080 monitor. The first two numbers are the top left corner of the screenshot, and the last two numbers are the bottom left corner of the screenshot.

# Like this program?
Do you like this program? If so I would really appreciate it if you would stop by and post something to my talk page on the Team Fortress 2 Wikipedia!

```wiki.teamfortress.com/wiki/User_talk:Lexzach```
