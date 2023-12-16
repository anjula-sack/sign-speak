import os
import tkinter as tk
import speech_recognition as sr
from PIL import Image, ImageTk

recognizer = sr.Recognizer()

#Speech recognition

def capture_voice_input():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    return audio

def convert_voice_to_text(audio):
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        text = ""
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        text = ""
        print("Error; {0}".format(e))
    return text

def process_voice_command(text):
    if "goodbye" in text.lower():
        print("Command Recognized....")
        print("Closing application....")
        return True
    


    

def text_to_asl(text):
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

    for char in text.lower():
        img_path = os.path.join('images', asl_mapping.get(char, 'unknown.png'))
        img = Image.open(img_path)
        img = img.resize((100, 100), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)

        panel = tk.Label(root, image=img)
        panel.image = img
        panel.pack(side="left")

if __name__ == "__main__":
    
    end_program = False
    while not end_program:
        audio = capture_voice_input()
        text = convert_voice_to_text(audio)
        end_program = process_voice_command(text)

        if text != "" and text != "goodbye" :
            root = tk.Tk()
            root.title("ASL Fingerspelling")
            text_to_asl(text)
            root.mainloop()
        
    

    
    

    

    

