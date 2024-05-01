import tkinter as tk
from tkinter import ttk
import configparser
class SettingsUI:
    def __init__(self, master):
        self.master = master
        master.title("Speech Recognizer Settings")

        master.geometry("500x300")  # Set the size of the window

        # Center the window
        self.center_window(500, 300)

        master.grid_columnconfigure(1, weight=1)  # Make column 1 expandable
        master.grid_rowconfigure(0, weight=1)  # Make row 0 expandable
        master.grid_rowconfigure(1, weight=1)  # Make row 1 expandable
        master.grid_rowconfigure(2, weight=1)  # Make row 2 expandable
        master.grid_rowconfigure(3, weight=1)  # Make row 3 expandable

        # load settings
        self.config = configparser.ConfigParser()
        self.config.read('settings.ini')
        self.load_settings()

        # Wake word entry
        self.wake_word_label = tk.Label(master, text="Wake Word:")
        self.wake_word_label.grid(row=0, column=0, sticky='w')
        self.wake_word_entry = tk.Entry(master, textvariable=self.wake_word)
        self.wake_word_entry.grid(row=0, column=1)

        # Threshold setting
        self.threshold_label = tk.Label(master, text="Volume Threshold:")
        self.threshold_label.grid(row=1, column=0, sticky='w')
        self.threshold_entry = tk.Entry(master, textvariable=self.threshold)
        self.threshold_entry.grid(row=1, column=1)

        self.model_label = tk.Label(master, text="Model Type:")
        self.model_label.grid(row=2, column=0, sticky='w')
        self.model_type = tk.StringVar()
        self.model_dropdown = ttk.Combobox(master, textvariable=self.model_type)
        self.model_dropdown['values'] = ('small', 'large', 'larger')
        self.model_dropdown.grid(row=2, column=1)
        self.model_dropdown.current(0)  # Set default to 'small'

        # Save Button
        self.save_button = tk.Button(master, text="Save", command=self.save_settings)
        self.save_button.grid(row=3, column=1, sticky='e')

    def load_settings(self):
        self.wake_word = tk.StringVar(value=self.config['DEFAULT'].get('WakeWord', 'activate'))
        self.threshold = tk.DoubleVar(value=float(self.config['DEFAULT'].get('Threshold', 500)))
        self.model_type = tk.StringVar(value=self.config['DEFAULT'].get('Model_type', 'small'))

    def save_settings(self):
        config = configparser.ConfigParser()
        config['DEFAULT'] = {
            'WakeWord': self.wake_word.get(),
            'Threshold': str(self.threshold.get()),
            'Model_type': str(self.model_type.get())
        }
        with open('settings.ini', 'w') as configfile:
            config.write(configfile)
        print("Settings saved")

    def center_window(self, width=500, height=300):
        # Get screen width and height
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Calculate position x, y
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.master.geometry(f'{width}x{height}+{x}+{y}')

def main():
    root = tk.Tk()
    gui = SettingsUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
