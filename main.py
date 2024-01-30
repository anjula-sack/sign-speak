import os
import tkinter as tk
from tkinter import ttk
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

def hide_error_label():
    error_label.config(text="")  # Clear the error label

def convert_voice_to_text(audio):
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        error_label.config(text="Sorry, I didn't understand that.")
        root.after(2000, hide_error_label)
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
        '0': '0.jpg',
        '1': '1.jpg',
        '2': '2.jpg',
        '3': '3.jpg',
        '4': '4.jpg',
        '5': '5.jpg',
        '6': '6.jpg',
        '7': '7.jpg',
        '8': '8.jpg',
        '9': '9.jpg',  
    }

    if index < len(text):
        char = text[index].lower()
        img_path = os.path.join('images', asl_mapping.get(char, 'unknown.png'))
        img = Image.open(img_path)
        img = img.resize((400, 400), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)

        panel.config(image=img)
        panel.image = img

        root.after(400, lambda: text_to_asl(text, index + 1))
    else:
        # After displaying all images, reset the label
        panel.config(image="")
        panel.image = None
        loading_label.config(text="")  # Reset loading text
        voice_rec_label.config(text="")


def start_stop_button():
    global listening
    if listening:
        listening = False
        
        style.configure("Rounded.TButton", foreground="green")
        start_stop_btn.config(text="Start Listening")
        loading_label.config(text="Loading...", fg="black")  # Show loading text only after stopping
        mic_label.config(image=mic_inactive_img)
        threading.Thread(target=listen_and_process).start()
    else:
        listening = True
        
        style.configure("Rounded.TButton", foreground="red")
        start_stop_btn.config(text="Stop Listening")
        loading_label.config(text="", fg="black")  # Clear loading text
        mic_label.config(image=mic_active_img)
        threading.Thread(target=listen_and_process).start()


def listen_and_process():
    global end_program
    if listening and not end_program:
        audio = capture_voice_input()
        text = convert_voice_to_text(audio)
        
        end_program = process_voice_command(text)
        text_to_asl(text)
        loading_label.config(text="", fg="black")  # Clear loading text when processing is done
        voice_rec_label.config(text=text)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sign Speak")

    root.geometry("1920x1080")  # Set a fixed window size

    listening = False
    end_program = False

    # Use ttk.Style to round the edges of the button
    style = ttk.Style()
    style.configure("Rounded.TButton",  highlightthickness="0", relief="flat", foreground="green", padding=(10, 20), font=("Helvetica", 16))

    start_stop_btn = ttk.Button(root, text="Start Listening", command=start_stop_button, style="Rounded.TButton")
    start_stop_btn.pack(pady=10)
    mic_active_img = ImageTk.PhotoImage(Image.open("images/active_mic.png").resize((40, 40)))
    mic_inactive_img = ImageTk.PhotoImage(Image.open("images/inactive_mic.png").resize((40, 40)))
    mic_label = tk.Label(root, image=mic_inactive_img)
    mic_label.pack(pady=4)

    voice_rec_label = tk.Label(root, text="", fg="black",font=("Helvetica",14))
    voice_rec_label.pack()

    panel = tk.Label(root)
    panel.pack(side="top", pady=10)


    loading_label = tk.Label(root, text="", fg="black",font=("Helvetica",14))
    loading_label.pack()

    error_label = tk.Label(root, text="", fg="black",font=("Helvetica",14))
    error_label.pack()

    # Add instruction panel 
    instruction_panel = tk.Label(root, text="Instructions: Speak into the microphone to convert your speech to ASL images.\n"
                                        "Click 'Start Listening' to begin, and 'Stop Listening' to stop.", 
                            fg="#333", font=("Helvetica", 16))  
    instruction_panel.pack(side="bottom", pady=10)

    root.mainloop()
