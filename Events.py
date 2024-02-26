import pyautogui
import subprocess
from ApplicationPaths import ApplicationPaths
screenWidth, screenHeight = pyautogui.size()
print(pyautogui.size())
print(screenWidth)
print(screenHeight)


# Top Left = (0,0)
# Top Right = (screedWidth, 0)
# BottomLeft = (0, screenHeight)
# BottomRight = (screenWidth, screenHeight)

def openApplication(name):
    subprocess.Popen(ApplicationPaths[name])

def closeApplication():
    # ensure that the notepad is the active window
    return

def copy():
    pyautogui.hotkey('ctrl', 'c')

def paste():
    pyautogui.hotkey('ctrl', 'v')

def cut():
    pyautogui.hotkey('ctrl', 'x')

def selectAll():
    pyautogui.hotkey('ctrl', 'a')

def click():
    pyautogui.click()

def doubleClick():
    pyautogui.doubleClick()

def selectWord():
    pyautogui.doubleClick()

def selectLine():
    pyautogui.tripleClick()

def moveTopLeft():
    pyautogui.moveTo(0, 0)

def moveTopRight():
    pyautogui.moveTo(screenWidth, 0)

def moveBottomLeft():
    pyautogui.moveTo(0, screenHeight)

def moveBottomRight():
    pyautogui.moveTo(screenWidth, screenHeight)

def moveToMiddle():
    pyautogui.moveTo(screenWidth / 2, screenHeight / 2)

def moveUp():
    currX, currY = pyautogui.position()
    pyautogui.moveTo(currX, currY - (0.05 * screenHeight))
def moveDown():
    currX, currY = pyautogui.position()
    pyautogui.moveTo(currX, currY +  (0.05 * screenHeight))
def moveRight():
    currX, currY = pyautogui.position()
    pyautogui.moveTo(currX + (0.05 * screenWidth), currY)
def moveLeft():
    currX, currY = pyautogui.position()
    pyautogui.moveTo(currX - (0.05 * screenWidth), currY)

def moveUpSmall():
    currX, currY = pyautogui.position()
    pyautogui.moveTo(currX, currY - (0.01 * screenHeight))
def moveDownSmall():
    currX, currY = pyautogui.position()
    pyautogui.moveTo(currX, currY +  (0.01 * screenHeight))
def moveRightSmall():
    currX, currY = pyautogui.position()
    pyautogui.moveTo(currX + (0.01 * screenWidth), currY)
def moveLeftSmall():
    currX, currY = pyautogui.position()
    pyautogui.moveTo(currX - (0.01 * screenWidth), currY)

def arrowKeyUp():
    pyautogui.press('up')

def arrowKeyDown():
    pyautogui.press('down')

def arrowKeyRight():
    pyautogui.press('left')

def arrowKeyLeft():
    pyautogui.press('right')

# FOR MOVEMENT MAKE SOME ALERT SYSTEM THAT TELLS THE USER THAT THE POSITION IS OUT OF BOUNDS OR OFF THE
# CURRENT APPLICATION WINDOW
#Make functions for moving select lines up,down,left, right
#Make function for new line and tab (indention)
# Make function for saving, saving as, and opening specific files.
# Scroll Function
# Make a function for writing text
# Function for selecting text??
#openApplication("NotePad")
#pyautogui.mouseDown()
# for i in range(5):
currX, currY = pyautogui.position()

#pyautogui.mouseUp()

# For text selection
# The drag method doesn't work how I want it to so I might rewrite it.
# It seems using shift and the arrow keys work well, although that would be tedious to do many times for the speaker
# I could just hold down shift and have the user move their mouse as well
# Or I could just have them hold the mouse down and then move to where they want to go and then release the mouse.
