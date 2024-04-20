from tkinter import *
from tkinter import messagebox
import parser
root=Tk()
root.resizable(height = None, width = None)

root.title('Calculator')

display=Entry(root,bg='sky blue',bd=4,justify=RIGHT,relief=SUNKEN)
display.grid(row=1,columnspan=15,sticky="NSEW")

#Geting input on button click an vie in display entry
i=0
def get_var(n):
    global i
    display.insert(i,n)
    i+=1

def clear_all():
    display.delete(0,END)

def back():
    full_str=display.get()
    if len(full_str):
        new_str=full_str[:-1]
        clear_all()
        display.insert(0,new_str)
    else:
        clear_all()
        display.insert(0,'Error')

def get_op(op):
    global i
    length=len(op)
    display.insert(i,op)
    i+=length

def equal():
    full_string=display.get()
    try:
        a=parser.expr(full_string).compile()
        result=eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,'Re check and enter')


#Used for dynamic sizing of calculator
Grid.rowconfigure(root, 0, weight=1)
Grid.rowconfigure(root, 1, weight=1)
Grid.rowconfigure(root, 2, weight=1)
Grid.rowconfigure(root, 3, weight=1)
Grid.rowconfigure(root, 4, weight=1)
Grid.rowconfigure(root, 5, weight=1)

Grid.columnconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 1, weight=1)
Grid.columnconfigure(root, 2, weight=1)
Grid.columnconfigure(root, 3, weight=1)


#Creating buttons
Button(root,text='  %',command=lambda :get_op('%'),width=5,height=2,bg='#96d6a7').grid(row=2,column=0,sticky="NSEW")
Button(root,text='X^2',command=lambda :get_op("**2"),width=5,height=2,bg='#96d6a7').grid(row=2,column=1,sticky="NSEW")
Button(root,text=' AC',command=lambda :clear_all(),width=5,height=2,bg='#96d6a7').grid(row=2,column=2,sticky="NSEW")
Button(root,text=' <-',command=lambda :back(),width=5,height=2,bg='#96d6a7').grid(row=2,column=3,sticky="NSEW")

Button(root,text='  7',command=lambda :get_var(7),width=5,height=2,bg='#a1d4c9').grid(row=3,column=0,sticky="NSEW")
Button(root,text='  8',command=lambda :get_var(8),width=5,height=2,bg='#a1d4c9').grid(row=3,column=1,sticky="NSEW")
Button(root,text='  9',command=lambda :get_var(9),width=5,height=2,bg='#a1d4c9').grid(row=3,column=2,sticky="NSEW")
Button(root,text='  *',command=lambda :get_op('*'),width=5,height=2,bg='#96d6a7').grid(row=3,column=3,sticky="NSEW")

Button(root,text='  4',command=lambda :get_var(4),width=5,height=2,bg='#a1d4c9').grid(row=4,column=0,sticky="NSEW")
Button(root,text='  5',command=lambda :get_var(5),width=5,height=2,bg='#a1d4c9').grid(row=4,column=1,sticky="NSEW")
Button(root,text='  6',command=lambda :get_var(6),width=5,height=2,bg='#a1d4c9').grid(row=4,column=2,sticky="NSEW")
Button(root,text='  -',command=lambda :get_op('-'),width=5,height=2,bg='#96d6a7').grid(row=4,column=3,sticky="NSEW")

Button(root,text='  1',command=lambda :get_var(1),width=5,height=2,bg='#a1d4c9').grid(row=5,column=0,sticky="NSEW")
Button(root,text='  2',command=lambda :get_var(2),width=5,height=2,bg='#a1d4c9').grid(row=5,column=1,sticky="NSEW")
Button(root,text='  3',command=lambda :get_var(3),width=5,height=2,bg='#a1d4c9').grid(row=5,column=2,sticky="NSEW")
Button(root,text='  +',command=lambda :get_op('+'),width=5,height=2,bg='#96d6a7').grid(row=5,column=3,sticky="NSEW")

Button(root,text='  0',command=lambda :get_var(0),width=5,height=2,bg='#a1d4c9').grid(row=6,column=0,sticky="NSEW")
Button(root,text='  .',command=lambda :get_op("."),width=5,height=2,bg='#96d6a7').grid(row=6,column=1,sticky="NSEW")
Button(root,text=' Pi',command=lambda :get_op('* 3.14'),width=5,height=2,bg='#96d6a7').grid(row=6,column=2,sticky="NSEW")
Button(root,text='  /',command=lambda :get_op('/'),width=5,height=2,bg='#96d6a7').grid(row=6,column=3,sticky="NSEW")

Button(root,text='  (',command=lambda :get_op("("),width=5,height=2,bg='#96d6a7').grid(row=7,column=0,sticky="NSEW")
Button(root,text='  )',command=lambda :get_op(')'),width=5,height=2,bg='#96d6a7').grid(row=7,column=1,sticky="NSEW")
Button(root,text='Exp',command=lambda :get_op("**"),width=5,height=2,bg='#96d6a7').grid(row=7,column=2,sticky="NSEW")

Button(root,text='  =',command=lambda :equal(),width=5,height=2,bg='#60a697').grid(row=7,column=3,sticky="NSEW")
root.mainloop()