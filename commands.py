import pyautogui
import time
# Define a dictionary mapping commands to functions
# the model wil be listening but not receiving anything unless Ok Kalsalingam is said
# have a queue for the commands
# figure out how to undo certain commands
# there should be a validation function for each command, 
# go through all the possible test cases
# figure out a way to display that the command has been sucessfully executed 
# have like a button that flashes green/red on top of the screen, this could take extra space
# make sure that NotePad is the primary window
# have a function that checks if the window is open, if not then open it
# values in dictionary can be the hotkey itself no need for a command
command_dict = {
    "dictate": dictate,
    "move cursor to beginning": move_to_beginning,
    "move cursor to end": move_to_end,
    "copy": copy,
    "cut": cut,
    "paste": paste,
    "undo": undo,
    "redo": redo,
    "select all": select_all,
    "bold": bold,
    "italicize": italicize,
    "underline": underline,
    "save document": save_document,
    "close document": close_document,
    "print document": print_document,
    "rename document": rename_document,
    "duplicate document": duplicate_document,
    "new document": new_document,
    "insert": insert,
    "attach files": attach_files,
    "add link": add_link,
    "open file": open_file,
    "find": find,
    "replace": replace,
    "zoom in": zoom_in,
    "zoom out": zoom_out,
    "increase font size": increase_font_size,
    "decrease font size": decrease_font_size,
    "align left": align_left,
    "align center": align_center,
    "align right": align_right,
    "page setup": page_setup,
    "print preview": print_preview
}

def start_command(command):
    if command == "Ok Kalasalingam":
        while True:
            recognize_speech() 
    
def execute_command(command):
    # Check if the recognized text matches any command in the command dictionary
    if command in command_dict:
        # Execute the corresponding function
        command_dict[command]()
    else:
        print("Command not recognized.")
        
def type_into_notepad(text):
    # Bring the Notepad window to the foreground
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.5)  # Wait for Notepad to activate
    
    # Type the text into Notepa 
    pyautogui.typewrite(text)






