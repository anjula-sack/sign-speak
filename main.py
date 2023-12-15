import os
import tkinter as tk
from PIL import Image, ImageTk

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
    input_text = input("Enter text to convert to ASL: ")

    root = tk.Tk()
    root.title("ASL Fingerspelling")

    text_to_asl(input_text)

    root.mainloop()

