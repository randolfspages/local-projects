from tkinter import *
import customtkinter
from gtts import gTTS
import os

# setting the appearance mode
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')


root = customtkinter.CTk()
root.title('TEXT2SPEECH APP')
root.geometry('400x350')


# text_input = open('text_input.txt', 'r').read()

def reset():
    for cell in root.winfo_children():
        cell.destroy()
        app()


def app():
    def click2read():
        text = textbox.get('0.1', END)
        language = 'en'
        output = gTTS(text=text, lang=language, slow=False)
        output.save('output.mp3')
        os.system('afplay output.mp3')
        reset()
    
    
    
# frame = customtkinter.CTkFrame(root)
# frame.pack(pady=60, padx=60, fill='both', expand=True)


    canvas = customtkinter.CTkCanvas(root, width=400, height=350)
    canvas.pack()

    textbox = customtkinter.CTkTextbox(root, width=200, height=100, bg_color='#D2CECD', 
                                       scrollbar_button_color='blue', scrollbar_button_hover_color='light-blue',
                                       corner_radius=2, border_color='red')
    canvas.create_window(200, 140, window=textbox)

    button = customtkinter.CTkButton(root, text='READ TEXT', command=click2read)
    canvas.create_window(200, 230, window=button)

app()
root.mainloop()