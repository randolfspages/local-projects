import customtkinter
from tkinter import filedialog
from compressModule import compress, decompress


# setting the appearance mode

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.title('File Compressor')
root.geometry('250x200')

     
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=30, padx=15, fill='both', expand=True)


    
def compression(i,o):
    compress(i,o)
    
def openfile():
    filename = filedialog.askopenfilename(initialdir='/', title='Select file to be compressed')
    return filename

label = customtkinter.CTkLabel(master=frame, text='Click SELECT \nto Input and COMPRESS File')
label.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text='SELECT', command=lambda:compression(openfile(), 'compressed.txt'))
button.pack(pady=12, padx=10)


root.mainloop()