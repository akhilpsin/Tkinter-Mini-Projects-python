from gtts import gTTS
import os
from tkinter import *
root=Tk()


root.title("Convert Text to Audio")


canvas=Canvas(root,width=300,height=250)
canvas.pack()

def txt_sp():
    text=entry.get()
    output = gTTS(text=text, lang='en', slow=False)
    output.save("audio_eng.mp4")
    os.system('start audio_eng.mp4')

entry=Entry(root)
canvas.create_window(150,150,window=entry, width=250,height=30)

btn=Button(root,text="Convert To Audio",command=txt_sp,fg = 'black',bg = 'light green')


canvas.create_window(200,230,window=btn)

root.mainloop()



