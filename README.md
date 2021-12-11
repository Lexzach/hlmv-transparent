Version 2.5

## HLMV Transparent
This is a program specifically designed for the Team Fortress 2 Wiki. It allows perfect transparent images to be easily and automatically created at the push of a button using the out of the box Half-Life Model Viewer program.

**IF YOU NOTICE BLACK SPOTS ON THE RENDERED IMAGE, MAKE SURE YOU DISABLE FILTERING OR ANY OTHER POST-PROCESSING EFFECTS YOUR GPU IS APPLYING TO HLMV.**

# Download & Setup
1. Click the green "Code" button and select "Download ZIP"
2. Extract to prefered destination
3. Run either `HLMV Transparent.exe` or `HLMV Cropper.exe` depending on what editing you need done

Feel free to contact me over Discord at `Lexzach#3215`, and I'll be glad to help you set it up.

# How to use in manual mode:

1. Take two screenshots in HLMV, one with the white background color and the other with the black background color. Use window capture, as these screenshots **must** be the same size.

2. Name the screenshot with the white background as `w0.png` and the black background `b0.png`. If you want to do multiple images at the same time, continue to name the images as mentioned above, but change the number from 0 to 1 then to 2, and so on.
As an example, if I wanted to do 2 white images and 2 black images, I would do the following:
`w0.png`
`b0.png`
`w1.png`
`b1.png`
...and when running the program I would type in `2` pairs when prompted.

3. Put those screenshots into the folder labeled `Rendering Folder`.

4. Run the program titled `HLMV Transparent.exe`.

5. Type out the amount of pairs you want to render. (ex. if you have `1` white image and `1` black image that would be `1` pair)

# How to use in automatic mode:

**Make sure you change `autoScreenshot` to `true` inside `config.txt`**

1. Run the program titled `HLMV Transparent.exe`.

2. Return to HLMV and press `S` to take a screenshot. (This will move your mouse around)

3. Press the `S` key to take as many screenshots as you wish.

4. Press `P` to finish and start rendering.

# How to use Transparent Cropper script

1. Place any transparent images that need to be shrunk into the `Cropping Folder` folder.

2. Run the program titled `HLMV Cropper.exe`.

3. Press the `crop` button to crop the images.

# Config.txt
- `autoCrop` - Automatically crops the transparent image down to its smallest possible size while keeping all aspects of the image intact.

- `deleteTempFiles` - Automatically clean up temporary files that are generated during operation.

- `autoScreenshot` - Assuming you have a 1920x1080 monitor, and HLMV is maximized (press the square on Windows), the program will automatically move your mouse around to take a screenshot far faster than a human could, after taking the amount of screenshots that the user wants to take, the program will then automatically render them. **REMEMBER: THIS SETTING WILL CONTROL YOUR MOUSE, I AM NOT RESPONSIBLE FOR ANY DAMAGES THAT COULD BE CAUSED BY THIS!!! YOU HAVE BEEN WARNED!**

- `screenshotSizes` - Adjust the size of the screenshot area. This is already coordinated for a 1920x1080 monitor. The first two numbers are the top left corner of the screenshot, and the last two numbers are the bottom left corner of the screenshot.

- `edgeSmoothing` - Adjust how much the program smooths edges, `0` is off. The default is `1.3`. Keep in mind that edge smoothing may make small objects such as wires look much worse in some instances.

# Like this program?
Do you like this program? If so I would really appreciate it if you would stop by and post something to my talk page on the Team Fortress 2 Wikipedia!

```wiki.teamfortress.com/wiki/User_talk:Lexzach```



# [ADVANCED] Running the pre-built version

## Dependencies:

- Python 3.8.6 `www.python.org/downloads/release/python-386/`
- OpenCV `pip install opencv-python`
- Pillow `pip install pillow`
- Pyautogui `pip install PyAutoGUI`
- Keyboard `pip install keyboard`
- SciKit `pip install scikit-image`

Alternatively, you can run the command `pip install -r requirements.txt` to automatically install the dependencies.

## How to install:

- Download Python 3.8.6 from `www.python.org/downloads/release/python-386/`
- Download HLMV Transparent ZIP file from this GitHub
- Extract ZIP download to your prefered destination.
- Open the `Command prompt`.
- Navigate to the folder that you extracted the program to.
- Click at the top of the Windows Explorer that shows the path, it should look something like `This PC > Downloads > hlmv-transparent-main`. Once clicked, the text should turn blue.
- Copy the text and return to the Command prompt.
- Type in `cd` plus a space, and then right click the Command prompt to paste the text, then press enter to run.
- Type in `pip install -r requirements.txt` and run it. If this displays an error saying that `pip is not an identified command`, please refer to [this](https://appuals.com/fix-pip-is-not-recognized-as-an-internal-or-external-command/) guide.
- Now your program should be setup, close the command prompt and return to the file explorer.
- Configure `config.txt` to adjust any settings you want.
- Double-click `hlmv-transparent.py` to start the program.
