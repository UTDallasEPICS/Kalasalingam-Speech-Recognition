import sys
from vosk import Model, KaldiRecognizer
import pyaudio
import json
import threading
import numpy as np
import configparser
import tkinter as tk
from settingsUI import settingsUI


class SpeechRecognizer(threading.Thread):
    def __init__(self, command_executor, sample_rate=16000, frames_per_buffer=2048): # 1024 or 8192
        super().__init__()

        self.sample_rate = sample_rate
        self.frames_per_buffer = frames_per_buffer
        self.command_executor = command_executor

        # Default values for settingsUI app for user
        self.wake_word = 'activate'
        self.threshold = 500
        self.model_type = 'small'

        self.run_settings_ui()
        self.load_settings()
        model_paths = {
            'small': r"C:\Users\arsh0\PycharmProjects\kalasalingam\vosk-model-small-en-us-0.15",
            'large': r"C:\Users\arsh0\PycharmProjects\kalasalingam\model",
            'larger': r"C:\Users\arsh0\PycharmProjects\kalasalingam\vosk-model-en-us-0.42-gigaspeech"
        }
        self.model = Model(model_paths[self.model_type])
        self.recognizer = KaldiRecognizer(self.model, sample_rate)
        self.mic = pyaudio.PyAudio()
        self.stream = self.mic.open(format=pyaudio.paInt16, channels=1, rate=sample_rate, input=True,
                                    frames_per_buffer=frames_per_buffer)
        self.recognizing = False
        self.last_wake_time = 0

        self.muted = False
        self.transcriptions = []
        self.low_confidence_count = 0
        self.pending_termination = False

    def run_settings_ui(self):
        root = tk.Tk()
        app = settingsUI(root)
        root.mainloop()

    def load_settings(self):
        config = configparser.ConfigParser()
        config.read('settings.ini')
        self.model_type = config['DEFAULT'].get('Model_type', 'small')
        self.wake_word = config['DEFAULT'].get('WakeWord', 'activate')
        self.threshold = float(config['DEFAULT'].get('Threshold', str(500)))

        print(
            f"Loaded settings: Wake Word={self.wake_word}, Threshold={self.threshold}, Model_Type={self.model_type}")

    def run(self):
        self.stream.start_stream()
        self.recognize_speech()

    def stop(self):
        print("Stopping Program...")
        self.recognizing = False
        self.stream.stop_stream()
        self.stream.close()
        print("[SPEECH RECOGNITION HAS STOPPED]")
        sys.exit()

    def calculate_ambient_noise(self, duration=3):
        print("Calculating ambient noise. Please be silent...")
        total_noise = 0
        num_samples = 0
        for _ in range(int(self.sample_rate / self.frames_per_buffer * duration)):
            data = self.stream.read(self.frames_per_buffer, exception_on_overflow=False)
            np_data = np.frombuffer(data, dtype=np.int16)
            total_noise += np.sum(np.abs(np_data))
            num_samples += len(np_data)
        avg_noise = total_noise / num_samples
        self.threshold = avg_noise * 1.5  # Adjust the multiplier based on required sensitivity
        print(f"New threshold set to: {self.threshold}")

    def recognize_speech(self):
        self.calculate_ambient_noise()
        print(f"Listening for the wake word: {self.wake_word} or 'terminate' to end the program")
        self.pending_termination = False
        try:
            while True:  # Change to a continuous loop
                data = self.stream.read(4096, exception_on_overflow=False)
                data = np.frombuffer(data, dtype=np.int16)

                if len(data) == 0:
                    break

                if self.recognizer.AcceptWaveform(data.tostring()):
                    result = json.loads(self.recognizer.Result())
                    res = result['text']
                    print(f"Detected: {res}")

                    if self.wake_word in res and not self.recognizing:
                        print("Wake word detected. Recognition activated.")
                        print("Waiting for next command....")
                        self.recognizing = True
                        continue

                    if "terminate" in res and not self.pending_termination:
                        self.pending_termination = True
                        print("Termination requested. Say 'yes please terminate' to confirm.")
                        continue

                    if "yes please terminate" in res and self.pending_termination:
                        print("Termination confirmed. Stopping recognition.")
                        self.stop()
                        break

                    if self.recognizing:
                        print(f"Final: {res}")
                        self.command_executor.execute_command(res)

        except KeyboardInterrupt:
            print("Program terminated by user")
            self.stop()