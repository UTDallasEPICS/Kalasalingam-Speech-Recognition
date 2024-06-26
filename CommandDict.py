#import Events
from Events2 import ApplicationControl as Events
command_dict = {
    # "move cursor to beginning": Events.move_to_beginning,
    # "move cursor to end": Events.move_to_end,
    "focus window": Events.focus_window,
    "click": Events.click,
    "copy": Events.copy,
    "cut": Events.cut,
    "paste": Events.paste,
    "undo": Events.undo,
    "redo": Events.redo,
    "enter": Events.enter,
    "select all": Events.selectAll,
    "select word": Events.selectWord,
    "select line": Events.selectLine,
    "bold": Events.bold,
    "italicize": Events.italicize,
    "underline": Events.underline,
    "save document": Events.save_document,
    "backspace":Events.backspace,
    "back space": Events.backspace,
    "tab" : Events.tab,
    # "close document": Events.close_document,
    "print document": Events.print_document,
    # "rename document": Events.rename_document,
    # "duplicate document": Events.duplicate_document,
    "new document": Events.new_document,
    "insert": Events.insert,
    "close": Events.close_application,
    # "attach files": Events.attach_files,
    # "add link": Events.add_link,
     "open": Events.open_application,
    # "find": Events.find,
    # "replace": Events.replace,
    "zoom in": Events.zoom_in,
    "zoom out": Events.zoom_out,
    "increase font size": Events.increase_font_size,
    "decrease font size": Events.decrease_font_size,
    "move top left" : Events.moveTopLeft,
    "move bottom left" : Events.moveBottomLeft,
    "move top right" : Events.moveTopRight,
    "move bottom right" : Events.moveBottomRight,
    "move to middle": Events.moveToMiddle,
    "move up": Events.moveUp,
    "move down": Events.moveDown,
    "move left": Events.moveLeft,
    "move right": Events.moveRight,
    "move up small" : Events.moveUpSmall,
    "move down small" : Events.moveDownSmall,
    "move left small" : Events.moveLeftSmall,
    "move right small" : Events.moveRightSmall,
    "arrow key up" : Events.arrowKeyUp,
    "arrow key down": Events.arrowKeyDown,
    "arrow key left": Events.arrowKeyLeft,
    "arrow key right": Events.arrowKeyRight,
    "shift select up" : Events.shiftSelectUp,
    "shift select down" : Events.shiftSelectDown,
    # "align left": Events.align_left,
    # "align Center": Events.align_center,
    # "align right": Events.align_right,
    # "page setup": Events.page_setup,
    "start dictating": Events.toggle_dictation_mode,
    "stop dictating": Events.toggle_dictation_mode,
    "mute": Events.mute,
    "turn off mute": Events.unmute,
}