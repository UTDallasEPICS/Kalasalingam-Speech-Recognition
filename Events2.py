import threading
import pyautogui
from ApplicationPaths import ApplicationPaths
import subprocess
import platform
import pygetwindow as gw
import os, glob

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
        if platform.system() == 'Darwin':  # macOS
            subprocess.Popen(['osascript', '-e', 'tell application "TextEdit" to activate'])
        else:  # windows, linux
            all_windows = gw.getAllWindows()
            for win in all_windows:
                if 'Notepad' in win.title:
                    win.activate()
                    break

    def open_application(self):
        if platform.system() == 'Darwin':  # macOS
            subprocess.Popen(['osascript', '-e', 'tell application "TextEdit" to make new document'])
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
        if platform.system() == 'Darwin':  # macOS
            script = '''
            set docName to "Document"
            set docFolder to (path to documents folder as text) & "TTSFiles:"
            set docExtension to ".txt"
            
            if not (exists folder docFolder) then
                do shell script "mkdir -p " & quoted form of docFolder
            end if
            
            tell application "TextEdit"
                try
                    set docNumber to count of (get files of folder docFolder whose name starts with docName)
                    set docNumber to docNumber + 1
                    
                    set docPath to docFolder & docName & "-" & docNumber & docExtension
                    
                    save front document to file docPath
                    log "Document saved successfully at: " & docPath
                on error errMsg
                    log "Error saving document: " & errMsg
                end try
            end tell
            '''
            try:
                process = subprocess.Popen(['osascript', '-e', script], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                stdout, stderr = process.communicate()
                if stdout:
                    print(f"AppleScript output: {stdout.strip()}")
                if stderr:
                    print(f"AppleScript error: {stderr.strip()}")
            except Exception as e:
                print(f"Error executing AppleScript: {str(e)}")
        elif platform.system() == 'Windows':
            # Set the folder path for saving documents
            folder_path = os.path.expanduser('~/Documents/TTSFiles')

            # Create the folder if it doesn't exist
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Get the list of existing files in the folder
            existing_files = glob.glob(os.path.join(folder_path, 'Document-*.txt'))

            # Find the highest existing document number
            if existing_files:
                latest_file = max(existing_files, key=lambda x: int(x.split('-')[-1].split('.')[0]))
                doc_number = int(latest_file.split('-')[-1].split('.')[0]) + 1
            else:
                doc_number = 1

            # Construct the new document path
            new_doc_path = os.path.join(folder_path, f'Document-{doc_number}.txt')

            # Save the document using the new file path
            pyautogui.hotkey(MODIFIER_KEY, 's')  # Press Ctrl+S to open the Save dialog
            pyautogui.typewrite(new_doc_path)  # Type the new file path
            pyautogui.press('enter')  # Press Enter to save the document
        else:
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