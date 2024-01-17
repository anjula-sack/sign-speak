import os
import tkinter as tk
import speech_recognition as sr
from PIL import Image, ImageTk
import threading

recognizer = sr.Recognizer()

# Speech recognition

def capture_voice_input():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    return audio

def convert_voice_to_text(audio):
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError as e:
        print("Error; {0}".format(e))
        return ""

def process_voice_command(text):
    if "goodbye" in text.lower():
        print("Command Recognized....")
        print("Closing application....")
        return True
    return False

def text_to_asl(text, index=0):
    asl_mapping = {
        'a': 'a.jpg',
        'b': 'b.jpg',
        'c': 'c.jpg',
        'd': 'd.jpg',
        'e': 'e.jpg',
        'f': 'f.jpg',
        'g': 'g.jpg',
        'h': 'h.jpg',
        'i': 'i.jpg',
        'j': 'j.jpg',
        'k': 'k.jpg',
        'l': 'l.jpg',
        'm': 'm.jpg',
        'n': 'n.jpg',
        'o': 'o.jpg',
        'p': 'p.jpg',
        'q': 'q.jpg',
        'r': 'r.jpg',
        's': 's.jpg',
        't': 't.jpg',
        'u': 'u.jpg',
        'v': 'v.jpg',
        'w': 'w.jpg',
        'x': 'x.jpg',
        'y': 'y.jpg',
        'z': 'z.jpg',
    }

    if index < len(text):
        char = text[index].lower()
        img_path = os.path.join('images', asl_mapping.get(char, 'unknown.png'))
        img = Image.open(img_path)
        img = img.resize((100, 100), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)

        panel.config(image=img)
        panel.image = img

        root.after(400, lambda: text_to_asl(text, index + 1))
    else:
        # After displaying all images, reset the label
        panel.config(image="")
        panel.image = None
        loading_label.config(text="")  # Reset loading text

def start_stop_button():
    global listening
    if listening:
        listening = False
        start_stop_btn.config(text="Start Listening")
        loading_label.config(text="Loading...")  # Show loading text only after stopping
        threading.Thread(target=listen_and_process).start()
    else:
        listening = True
        start_stop_btn.config(text="Stop Listening")
        loading_label.config(text="")  # Clear loading text
        threading.Thread(target=listen_and_process).start()

def listen_and_process():
    global end_program
    if listening and not end_program:
        audio = capture_voice_input()
        text = convert_voice_to_text(audio)
        end_program = process_voice_command(text)
        text_to_asl(text)
        loading_label.config(text="")  # Clear loading text when processing is done

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sign Speak")

    listening = False
    end_program = False

    panel = tk.Label(root)
    panel.pack(side="left")

    loading_label = tk.Label(root, text="")
    loading_label.pack()

    start_stop_btn = tk.Button(root, text="Start Listening", command=start_stop_button)
    start_stop_btn.pack()

    root.mainloop()
