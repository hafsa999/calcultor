from tkinter import *


def clicked(num):
    first_num=e1.get()
    e1.delete(0,END)
    e1.insert(0,str(first_num)+str(num))
def add():
    first_num=e1.get()
    global old_Value
    old_Value=int(first_num)
    global math
    math="addition"
    e1.delete(0,END)
def minus():
    first_num=e1.get()
    global old_Value
    old_Value=int(first_num)
    global math
    math="minus"
    e1.delete(0,END)
def multi():
    first_num=e1.get()
    global old_Value
    old_Value=int(first_num)
    global math
    math="multiplication"
    e1.delete(0,END)
def div():
    first_num=e1.get()
    global old_Value
    old_Value=int(first_num)
    global math
    math="div"
    e1.delete(0,END)
def equal():
    if math=="addition":
        new_value=e1.get()
        e1.delete(0,END)
        e1.insert(0,int(old_Value)+int(new_value)) 
    if math=="minus":
        new_value=e1.get()
        e1.delete(0,END)
        e1.insert(0,int(old_Value)-int(new_value)) 
    if math=="multiplication":
        new_value=e1.get()
        e1.delete(0,END)
        e1.insert(0,int(old_Value)*int(new_value)) 
    if math=="div":
        new_value=e1.get()
        e1.delete(0,END)
        e1.insert(0,int(old_Value)/int(new_value)) 
def clear():
    e1.delete(0,END)  
loop=Tk()
loop.title("calculator")
loop.geometry("150x220")
myText=StringVar()
result=Label(loop,text="",textvariable=myText)
result.place(x=10,y=100)

e1=Entry(loop)
e1.place(x=10,y=10)
a=Button(loop,text="1",command=lambda:clicked(1))
a.place(x=10,y=140)
b=Button(loop,text="2",command=lambda:clicked(2))
b.place(x=40,y=140)
c=Button(loop,text="3",command=lambda:clicked(3))
c.place(x=70,y=140)
d=Button(loop,text="4",command=lambda:clicked(4))
d.place(x=10,y=100)
e=Button(loop,text="5",command=lambda:clicked(5))
e.place(x=40,y=100)
f=Button(loop,text="6",command=lambda:clicked(6))
f.place(x=70,y=100)
g=Button(loop,text="7",command=lambda:clicked(7))
g.place(x=10,y=60)
h=Button(loop,text="8",command=lambda:clicked(8))
h.place(x=40,y=60)
i=Button(loop,text="9",command=lambda:clicked(9))
i.place(x=70,y=60)
j=Button(loop,text="+",command=add)
j.place(x=110,y=100)
k=Button(loop,text="-",command=minus)
k.place(x=110,y=140)
l=Button(loop,text="x",command=multi)
l.place(x=110,y=60)
m=Button(loop,text="/",command=div)
m.place(x=110,y=30)
n=Button(loop,text="%")
n.place(x=10,y=180)
o=Button(loop,text="0",command=lambda:clicked(0))
o.place(x=40,y=180)
p=Button(loop,text=".",command=lambda:clicked("."))
p.place(x=70,y=180)
q=Button(loop,text="=",command=equal)
q.place(x=110,y=180)
s=Button(loop,text="clear",command=clear)
s.place(x=120,y=60)


mainloop()