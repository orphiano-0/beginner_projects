import pyttsx3 # install pyttsx3: pip install pyttsx3
import tkinter as tk

class window:
    def __init__(self):
        # window format of the gui
        self.root = tk.Tk()
        self.root.title("Text Speaker")
        self.root.geometry("500x300")

        self.label = tk.Label(self.root, text="Type what you want to hear!", font=('Arial', 15))
        self.label.pack(pady=10)

        self.textbox = tk.Text(self.root, font=('Arial', 13), height=5, wrap="word")
        self.textbox.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Speak", font=('Arial', 15), command=self.button_click)
        self.button.pack(pady=10)

        self.root.mainloop()

    def button_click(self):
        engine = pyttsx3.init()
        engine.say(self.textbox.get("1.0", tk.END))
        engine.runAndWait()

window()
