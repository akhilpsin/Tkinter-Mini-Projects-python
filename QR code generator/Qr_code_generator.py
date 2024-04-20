from tkinter import *
import pyqrcode
from PIL import ImageTk,Image

root=Tk()

def qr_generate():
    name = name_entry.get()
    link = link_entry.get()
    file_name=name+'.png'
    url=pyqrcode.create(link)
    url.png(file_name,scale=8)
    img=ImageTk.PhotoImage(Image.open(file_name))
    img_label=Label(image=img)
    img_label.image=img
    canvas.create_window(200,500,window=img_label)

#Creating a canvas
canvas=Canvas(root,width=400,height=600)
canvas.pack()

#adding labes, entry box and button to be on canvas
label1=Label(root,text='QR code generator',fg='green',font=('Arial',30))
name_label=Label(root,text='Link Name')
link_label=Label(root,text='Link')
name_entry=Entry(root)
link_entry=Entry(root)
btn=Button(text='Generate QR',command=qr_generate)

#including every elements in canvas
canvas.create_window(200,50,window=label1)
canvas.create_window(200,100,window=link_label)
canvas.create_window(200,120,window=link_entry)
canvas.create_window(200,160,window=name_label)
canvas.create_window(200,180,window=name_entry)
canvas.create_window(200,220,window=btn)

root.mainloop()
