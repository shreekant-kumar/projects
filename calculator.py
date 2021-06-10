from tkinter import *
from math import *
root=Tk()
root.title("simple calculator")
operator=""
text_input=StringVar()
e=Entry(root,width=35,borderwidth=5,textvariable=text_input,bg="powder blue",font=('arial',10,'bold'))
e.grid(row=0,column=0,columnspan=4,pady=10)
def button_click(number):
    global operator
    operator+=str(number)
    text_input.set(operator)

def button_clear():
    global operator
    operator=""
    text_input.set("")

def button_equal():
    global operator
    output=str(eval(operator))
    text_input.set(output)
    operator=""

button_1=Button(root,text="1",font=('arial',10,'bold'),padx=25,pady=15,fg="black",command=lambda:button_click(1))
button_2=Button(root,text="2",font=('arial',10,'bold'),padx=25,pady=15,fg="black",command=lambda:button_click(2))
button_3=Button(root,text="3",font=('arial',10,'bold'),padx=25,pady=15,fg="black",command=lambda:button_click(3))
button_4=Button(root,text="4",font=('arial',10,'bold'),padx=25,pady=15,fg="black",command=lambda:button_click(4))
button_5=Button(root,text="5",font=('arial',10,'bold'),padx=25,pady=15,fg="black",command=lambda:button_click(5))
button_6=Button(root,text="6",font=('arial',10,'bold'),padx=25,pady=15,fg="black",command=lambda:button_click(6))
button_7=Button(root,text="7",font=('arial',10,'bold'),padx=25,pady=15,fg="black",command=lambda:button_click(7))
button_8=Button(root,text="8",font=('arial',10,'bold'),padx=25,pady=15,fg="black",command=lambda:button_click(8))
button_9=Button(root,text="9",font=('arial',10,'bold'),padx=25,pady=15,fg="black",command=lambda:button_click(9))
button_0=Button(root,text="0",font=('arial',10,'bold'),padx=25,pady=15,fg="black",command=lambda:button_click(0))

button_add=Button(root,text="+",font=('arial',10,'bold'),padx=25,pady=15,fg="black",command=lambda:button_click("+"))
button_sub=Button(root,text="-",font=('arial',10,'bold'),padx=25,pady=15,fg="black",command=lambda:button_click("-"))
button_mul=Button(root,text="*",font=('arial',10,'bold'),padx=25,pady=15,fg="black",command=lambda:button_click("*"))
button_div=Button(root,text="/",font=('arial',10,'bold'),padx=25,pady=15,fg="black",command=lambda:button_click("/"))
button_left=Button(root,text="(",font=('arial',10,'bold'),padx=25,pady=15,fg="black",command=lambda:button_click("("))
button_right= Button(root,text=")",font=('arial',10,'bold'),padx=25,pady=15,fg="black",command=lambda:button_click(")"))
button_comma=Button(root,text=",",font=('arial',10,'bold'),padx=25,pady=15,fg="black",command=lambda:button_click(","))
button_sqrt=Button(root,text="sqrt",font=('arial',10,'bold'),padx=18,pady=15,fg="black",command=lambda:button_click("sqrt"))
button_log=Button(root,text="log",font=('arial',10,'bold'),padx=18,pady=15,fg="black",command=lambda:button_click("log"))
button_pow=Button(root,text="pow",font=('arial',10,'bold'),padx=18,pady=15,fg="black",command=lambda:button_click("pow"))

button_equal=Button(root,text="=",font=('arial',10,'bold'),padx=90,pady=15,fg="black",command=button_equal)
button_clear=Button(root,text="C",font=('arial',10,'bold'),padx=25,pady=15,fg="black",command=button_clear)
#put the buttons on screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_mul.grid(row=3,column=3)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_sub.grid(row=2,column=3)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_add.grid(row=1,column=3)

button_0.grid(row=4,column=0)
button_left.grid(row=4,column=1)
button_right.grid(row=4,column=2)
button_div.grid(row=4,column=3)


button_comma.grid(row=5,column=0)
button_pow.grid(row=5,column=1)
button_sqrt.grid(row=5,column=2)
button_log.grid(row=5,column=3)


button_equal.grid(row=6,column=1,columnspan=3)
button_clear.grid(row=6,column=0)
root.mainloop()