import threading
import pyautogui
from ApplicationPaths import ApplicationPaths
import subprocess
import platform
import pygetwindow as gw
pyautogui.FAILSAFE = False

if platform.system() == 'Darwin':  # macOS
    MODIFIER_KEY = 'command'
else:  # Default to 'ctrl' for Windows, Linux, and other OSes
    MODIFIER_KEY = 'ctrl'

class ApplicationControl(threading.Thread):
    def __init__(self, command_executor):
        super().__init__()
        self.command_executor = command_executor
        self.screenWidth, self.screenHeight = pyautogui.size()

    def focus_window(self):
        all_windows = gw.getAllWindows()
        for win in all_windows:
            if 'Notepad' in win.title:
                win.activate()
                break

    def open_application(self):
        if platform.system() == 'Darwin':  # macOS
            name = 'TextEdit'
        else:  # windows, linux
            name = 'NotePad'
        subprocess.Popen(ApplicationPaths[name])

    def close_application(self):
        if platform.system() == 'Darwin':  # macOS
            pyautogui.hotkey(MODIFIER_KEY, 'q')
        else:  # windows, linux
            pyautogui.hotkey('alt', 'f4')
        return

    def copy(self):
        pyautogui.hotkey(MODIFIER_KEY, 'c')

    def paste(self):
        pyautogui.hotkey(MODIFIER_KEY, 'v')

    def cut(self):
        pyautogui.hotkey(MODIFIER_KEY, 'x')

    def enter(self):
        pyautogui.press('enter')

    def backspace(self):
        pyautogui.press('backspace')

    def tab(self):
        pyautogui.press('tab')

    def selectAll(self):
        pyautogui.hotkey(MODIFIER_KEY, 'a')

    def insert(self):
        pyautogui.press('insert')

    def click(self):
        pyautogui.click()

    def rightClick(self):
        pyautogui.rightClick()

    def doubleClick(self):
        pyautogui.doubleClick()

    def selectWord(self):
        pyautogui.doubleClick()

    def selectLine(self):
        pyautogui.tripleClick()

    def shiftSelectUp(self):
        pyautogui.hotkey('shift', 'up')

    def shiftSelectDown(self):
        pyautogui.hotkey('shift', 'down')

    def moveTopLeft(self):
        pyautogui.moveTo(0, 0)

    def moveTopRight(self):
        pyautogui.moveTo(self.screenWidth, 0)

    def moveBottomLeft(self):
        pyautogui.moveTo(0, self.screenHeight)

    def moveBottomRight(self):
        pyautogui.moveTo(self.screenWidth, self.screenHeight)

    def moveToMiddle(self):
        pyautogui.moveTo(self.screenWidth / 2, self.screenHeight / 2)

    def moveUp(self):
        currX, currY = pyautogui.position()
        pyautogui.moveTo(currX, currY - (0.05 * self.screenHeight))

    def moveDown(self):
        currX, currY = pyautogui.position()
        pyautogui.moveTo(currX, currY + (0.05 * self.screenHeight))

    def moveRight(self):
        currX, currY = pyautogui.position()
        pyautogui.moveTo(currX + (0.05 * self.screenWidth), currY)

    def moveLeft(self):
        currX, currY = pyautogui.position()
        pyautogui.moveTo(currX - (0.05 * self.screenWidth), currY)

    def moveUpSmall(self):
        currX, currY = pyautogui.position()
        pyautogui.moveTo(currX, currY - (0.01 * self.screenHeight))

    def moveDownSmall(self):
        currX, currY = pyautogui.position()
        pyautogui.moveTo(currX, currY + (0.01 * self.screenHeight))

    def moveRightSmall(self):
        currX, currY = pyautogui.position()
        pyautogui.moveTo(currX + (0.01 * self.screenWidth), currY)

    def moveLeftSmall(self):
        currX, currY = pyautogui.position()
        pyautogui.moveTo(currX - (0.01 * self.screenWidth), currY)

    def arrowKeyUp(self):
        pyautogui.press('up')

    def arrowKeyDown(self):
        pyautogui.press('down')

    def arrowKeyRight(self):
        pyautogui.press('left')

    def arrowKeyLeft(self):
        pyautogui.press('right')

    def zoom_in(self):
        pyautogui.hotkey(MODIFIER_KEY, '+')

    def zoom_out(self):
        pyautogui.hotkey(MODIFIER_KEY, '-')

    def save_document(self):
        pyautogui.hotkey(MODIFIER_KEY, 's')

    def underline(self):
        pyautogui.hotkey(MODIFIER_KEY, 'u')

    def bold(self):
        pyautogui.hotkey(MODIFIER_KEY, 'b')

    def italicize(self):
        pyautogui.hotkey(MODIFIER_KEY, 'i')

    def increase_font_size(self):
        pyautogui.hotkey(MODIFIER_KEY, ']')

    def undo(self):
        pyautogui.hotkey(MODIFIER_KEY, 'z')

    def redo(self):
        pyautogui.hotkey(MODIFIER_KEY, 'y')

    def decrease_font_size(self):
        pyautogui.hotkey(MODIFIER_KEY, ']')

    def new_document(self):
        pyautogui.hotkey(MODIFIER_KEY, 'shift', 'n')

    def print_document(self):
        pyautogui.hotkey(MODIFIER_KEY, 'p')

    def toggle_dictation_mode(self):
        self.command_executor.toggle_dictation_mode()

    def dictate(self):
        self.command_executor.toggle_dictation_mode()

    def mute(self):
        self.command_executor.setMute(True)

    def unmute(self):
        self.command_executor.setMute(False)