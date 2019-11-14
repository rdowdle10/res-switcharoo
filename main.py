# This is a simple program that runs a resolution on a screen that isn't *normally* supported
# on a display panel. This was created to be used on a laptop with a horrid 1366x768 screen, but can technically
# be used on any laptop with the same resolution.

#@TODO: Have the app check for existing aspect ratios to mitigate mistakes.

from tkinter import *
import tkinter as tk
import os
intro="""Welcome to the Resolution Stretcher! This utility allows for someone to run an unsupported resolution on displays that do not support them. Please be careful regarding which modes you choose, as monitors can vary in aspect ratio.

NOTE: xorg must be running and xrandr must be installed"""

#Class for the actual window.
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    # This is where the main window components go.
    def init_window(self):
        # Section for grabbing screen information
        scrn_w = root.winfo_screenwidth()
        scrn_h = root.winfo_screenheight()
        scrn_aspect = str(round(scrn_w/scrn_h, 1))
        print("current screen resolution is: " + str(scrn_w) + "x" + str(scrn_h))
        print("aspect ratio value is: " + scrn_aspect)
        
        # Setting the window title.
        self.master.title("Resolution Stretcher")
        self.pack(fill=BOTH, expand=1)

        # Main menu section
        # Creating the "File" menu in the main menu
        menu = Menu(self.master)
        self.master.config(menu=menu)
        # Menu Object (file menu)
        file=Menu(menu)
        file.add_command(label="About")
        # Adding the actual "file" menu
        menu.add_cascade(label="File", menu=file)

        # Defining an exit button with its respective command.
        
        exitButton = Button(self, text="Quit", command=self.client_exit, width=20, justify=CENTER, state=NORMAL)
        exitButton.place(x=125, y=360)

        # Defining a label containing the description of the program
        introText = Label(root, text=intro, padx=10, pady=10, wraplength=400, justify=LEFT)
        introText.place(y=0)

        # Section for 16:9 
        standardWide = Label(root, text="16:9 Aspect Ratio", wraplength=400, padx=10, justify=LEFT)
        standardWide.place(y=110)

        # Button for 1366x768
        stdwidebutton1366x768 = Button(self, text="1366x768", command=self.switchres1366, state=NORMAL)
        stdwidebutton1366x768.place(x=10, y=130)

        #Checking to see if resolution is set to 1366x768 already
        #if scrn_w == 1366:
        #    stdwidebutton1366x768["state"] = "disabled"
        
        # Button for 1600x900
        btn1600res = Button(self, text="1600x900", command=self.switchres1600, state=NORMAL)
        btn1600res.place(x=10, y=160)

        # Checking to see if resolution is already set to 1600x900
        #if scrn_w == 1600:
        #    btn1600res["state"] = "disabled"

        # Button for 1920x1080
        btnfullhd = Button(self, text="1920x1080", command=self.switchres1920, state=NORMAL)
        btnfullhd.place(x=10, y=190)

        # Check to see if running in Full HD
        #if scrn_w == 1080:
        #    btnfullhd["state"] = "disabled"

    # Define an exit...
    def client_exit(self):
        exit()

    def switchres1366(self):
        os.popen("xrandr --output eDP1 --panning 1366x768 --scale 1x1")
    def switchres1600(self):
        os.popen("xrandr --output eDP1 --panning 1600x900 --scale 1.171x1.171")
    def switchres1920(self):
        os.popen("xrandr --output eDP1 --panning 1920x1080 --scale 1.406x1.406")

root = Tk()
app = Window(root)

# Set the client window's size.
root.geometry("420x400")
root.resizable(False, False)

# Initialize the application mainloop.
root.mainloop()