from tkinter import *
from numpy import size
from sqlalchemy import VARCHAR
import tkinter.font as font
try:
    global val;
    val = ""
    def test():
        print("test ok")
    def btnclick(number):
        global val
        val += str(number)
        print(val)
        data.set(val)
        return val

    def btnclear():
        global val
        val = ""
        data.set('')
        
        
    def btnequal():
        print(val)
        result = str(eval(val))
        data.set(result)
        
    root = Tk()
    root.title("Calculator")
    root.geometry("400x480")
    root.resizable(0,0)
    root.configure(bg='black')
    data = StringVar()
    # display = Frame(bg="black",fg='white',width=30,height=30)
    display = Entry(root,bd=10,textvariable=data,bg="black",fg='white',justify="right",font=("arial",26))
    display.grid(row=0,columnspan=4)
    btn7 = Button(root,text="7",bg="black",fg='white',font=("arial",30,'bold'),width=3,height=2,bd=1,borderwidth=0,command=lambda:btnclick(7))
    btn7.grid(column=0,row=1)
    #btn7['font'] = font.Font(size=20)
    btn8 = Button(root,text="8",bg="black",fg='white',font=("arial",30,'bold'),width=3,height=2,bd=12,borderwidth=0,command=lambda:btnclick(8))
    btn8.grid(column=1,row=1)
    btn9 = Button(root,text="9",bg="black",fg='white',font=("arial",30,'bold'),width=3,height=2,bd=12,borderwidth=0,command=lambda:btnclick(9))
    btn9.grid(column=2,row=1)
    btnadd = Button(root,text="+",bg="black",fg='white',font=("arial",30,'bold'),width=3,height=2,bd=12,borderwidth=0,command=lambda:btnclick("+"))
    btnadd.grid(column=3,row=1)

    btn4 = Button(root,text="4",bg="black",fg='white',font=("arial",30,'bold'),width=3,height=2,bd=12,borderwidth=0,command=lambda:btnclick(4))
    btn4.grid(column=0,row=2)
    btn5 = Button(root,text="5",bg="black",fg='white',font=("arial",30,'bold'),width=3,height=2,bd=12,borderwidth=0,command=lambda:btnclick(5))
    btn5.grid(column=1,row=2)
    btn6 = Button(root,text="6",bg="black",fg='white',font=("arial",30,'bold'),width=3,height=2,bd=12,borderwidth=0,command=lambda:btnclick(6))
    btn6.grid(column=2,row=2)
    btnmin = Button(root,text="-",bg="black",fg='white',font=("arial",30,'bold'),width=3,height=2,bd=12,borderwidth=0,command=lambda:btnclick("-"))
    btnmin.grid(column=3,row=2)

    btn1 = Button(root,text="1",bg="black",fg='white',font=("arial",30,'bold'),width=3,height=2,bd=12,borderwidth=0,command=lambda:btnclick(1))
    btn1.grid(column=0,row=3)
    btn2 = Button(root,text="2",bg="black",fg='white',font=("arial",30,'bold'),width=3,height=2,bd=12,borderwidth=0,command=lambda:btnclick(2))
    btn2.grid(column=1,row=3)
    btn3 = Button(root,text="3",bg="black",fg='white',font=("arial",30,'bold'),width=3,height=2,bd=12,borderwidth=0,command=lambda:btnclick(3))
    btn3.grid(column=2,row=3)
    btnmul = Button(root,text="X",bg="black",fg='white',font=("arial",30,'bold'),width=3,height=2,bd=12,borderwidth=0,command=lambda:btnclick("*"))
    btnmul.grid(column=3,row=3)

    btnc = Button(root,text="C",bg="black",fg='white',font=("arial",30,'bold'),width=3,height=2,bd=12,borderwidth=0,command=lambda:btnclear())
    btnc.grid(column=0,row=4)
    btn0 = Button(root,text="0",bg="black",fg='white',font=("arial",30,'bold'),width=3,height=2,bd=12,borderwidth=0,command=lambda:btnclick(0))
    btn0.grid(column=1,row=4)
    btnequ = Button(root,text="=",bg="black",fg='white',font=("arial",30,'bold'),width=3,height=2,bd=12,borderwidth=0,command=lambda:btnequal())
    btnequ.grid(column=2,row=4)
    btndiv = Button(root,text="/",bg="black",fg='white',font=("arial",30,'bold'),width=3,height=2,bd=12,borderwidth=0,command=lambda:btnclick("/"))
    btndiv.grid(column=3,row=4)
    root.mainloop()
except Exception:
    def err():
        data.set("Error")
    err()