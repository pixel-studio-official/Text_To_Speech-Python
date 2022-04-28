import tkinter as tk
import tkinter.filedialog as fd
import pyttsx3

app = tk.Tk()
app.title("Text To Speech")

ta = tk.Text(app)
ta.pack()

def speak():
    text = ta.get(1.0, "end-1c")
    voice = pyttsx3.init()
    voice.say(text)
    voice.runAndWait()
def speak_f():
    file_loc = fd.askopenfilename(filetypes=(
        ("Text Files", "*.txt"),
        ("All Files", "*.*"),
    ))
    print(file_loc)
    with open(file_loc, "r") as file:
        data = file.read()
    voice = pyttsx3.init()
    voice.say(data)
    voice.runAndWait()

btn = tk.Button(app, text="Speak", command=speak).pack()
file_btn = tk.Button(app, text="Speak From File", command=speak_f).pack()

app.mainloop()
