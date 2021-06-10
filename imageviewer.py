from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title("Image Viewer")
myimg1=ImageTk.PhotoImage(Image.open("D:/New folder/para.png"))
myimg2=ImageTk.PhotoImage(Image.open("D:/New folder/pic11.jpg"))
myimg3=ImageTk.PhotoImage(Image.open("D:/New folder/pic21.jpg"))
myimg4=ImageTk.PhotoImage(Image.open("D:/New folder/pic31.jpg"))
myimg5=ImageTk.PhotoImage(Image.open("D:/New folder/pic41.jpg"))
imagelist=[myimg1,myimg2,myimg3,myimg4,myimg5]

status=Label(root,text="Image 1 of "+ str(len(imagelist)),bd=1,relief=SUNKEN,anchor=E)

my_label=Label(image=myimg1)
my_label.grid(row=0,column=0,columnspan=3)

def forward(image_num):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label=Label(image=imagelist[image_num-1])
    button_forward=Button(root,text=">>",command=lambda:forward(image_num+1))
    button_back=Button(root,text="<<",command=lambda:back(image_num-1))
    if image_num==len(imagelist):
        button_forward=Button(root,text=">>",state=DISABLED)
    status=Label(root,text="Image "+ str(image_num)+ " of "+ str(len(imagelist)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)
    my_label.grid(row=0,column=0,columnspan=3)
    button_forward.grid(row=1,column=2)
    button_back.grid(row=1,column=0)



def back(image_num):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label=Label(image=imagelist[image_num-1])
    button_forward=Button(root,text=">>",command=lambda:forward(image_num+1))
    button_back=Button(root,text="<<",command=lambda:back(image_num-1))
    if image_num==1:
        button_back=Button(root,text="<<",state=DISABLED)
    status=Label(root,text="Image "+ str(image_num)+ " of "+ str(len(imagelist)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)
    my_label.grid(row=0,column=0,columnspan=3)
    button_forward.grid(row=1,column=2)
    button_back.grid(row=1,column=0)


button_back=Button(root,text="<<",command=lambda:back(2),state=DISABLED)
button_exit=Button(root,text="Exit Program",command=root.quit)
button_forward=Button(root,text=">>",command=lambda:forward(2))

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2,pady=10)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)
root.mainloop()