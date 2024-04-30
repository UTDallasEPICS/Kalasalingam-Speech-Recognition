import queue
import sys
import pyautogui
import time
import threading
from fuzzywuzzy import process
from Events2 import ApplicationControl
from SpeechReg import SpeechRecognizer
from CommandDict import command_dict
from fastpunct import FastPunct
from playsound import playsound
fp = FastPunct('english')
class CommandExecutor:
    def __init__(self, command_dict):
        self.events = None
        self.worker = None
        self.dictation_mode = False  # Track dictation mode
        self.command_dict = command_dict
        self.init_events()
        self.commands_queue = queue.Queue()
        self.init_worker()
        self.process_commands()
        self.low_confidence_count = 0
        self.muted = False

    def init_worker(self):
        self.worker = SpeechRecognizer(self)
        self.wake_word = self.worker.wake_word
        self.worker.daemon = True
        self.worker.start()

    def init_events(self):
        self.events = ApplicationControl(self)
        self.events.daemon = True
        self.events.start()

    def setMute(self, isMuted):
        self.muted = isMuted
        print(isMuted and "[MUTED MODE ON]" or "[MUTED MODE OFF]")

    def toggle_dictation_mode(self):
        self.dictation_mode = not self.dictation_mode
        print(self.dictation_mode and "[Dictation mode: ON]" or "[Dictation mode: OFF]")

    def type_text(self, text):
        time.sleep(0.1)  # Wait a bit for TextEdit to be ready
        newText = fp.punct([text])
        pyautogui.typewrite(newText[0] + ' ')  # Type the text

    def playValidSound(self):
        playsound(r"C:\Users\Xodack Sigmus\PycharmProjects\STT_Testing\ValidSoundEffect.mp3")

    def playInvalidSound(self):
        playsound(r"C:\Users\Xodack Sigmus\PycharmProjects\STT_Testing\ErrorSoundEffect.mp3")

    def execute_command(self, command):
        try:
            if self.muted and not command in "unmute":
                return
            if self.dictation_mode:
                if "stop dictating" in command:
                    self.command_dict["stop dictating"](self.events)
                    self.playValidSound()
                else:
                    self.type_text(command)
            elif not self.dictation_mode:
                closest_match, confidence = process.extractOne(command, self.command_dict.keys())
                if confidence > 90:  # You can adjust the confidence level as needed
                    self.low_confidence_count = 0
                    print(
                        f"Closest command match: '{closest_match}' with confidence {confidence}. Executing command.")
                    self.command_dict[closest_match](self.events)  # Modified to pass self if needed
                    self.playValidSound()
                elif closest_match == 'activate' or closest_match == 'terminate':
                    pass
                else:
                    print(f"No confident command match found for '{command}'. Please try again.")
                    self.playInvalidSound()
                    self.low_confidence_count += 1
                    print(f"Incorrect Words: {self.low_confidence_count}")
                    if self.low_confidence_count >= 5:
                        self.setMute(True)
                        self.low_confidence_count = 0
                        print("Automatic mute activated due to low confidence commands.")
        except Exception as e:
            self.playInvalidSound()
            print(f"An error occurred: {e}")

    def process_commands(self):
        def command_processor():
            while True:
                command = self.commands_queue.get()
                self.execute_command(command)
                self.commands_queue.task_done()

        processor_thread = threading.Thread(target=command_processor)
        processor_thread.daemon = True
        processor_thread.start()


if __name__ == "__main__":
    print("Starting Program...")
    executor = CommandExecutor(command_dict)
    try:
        while True:  # Keep the main thread alive
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program terminated by user")
        sys.exit()
