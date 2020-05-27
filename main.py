from tkinter import *
import tkinter.filedialog as fdialog
import cv2
import stitch
import numpy as np
import random
import matplotlib.pyplot as plt

def browseimage_left():
    filename = fdialog.askopenfilename()
    imgleft = cv2.imread(filename)
    imgleft=cv2.resize(imgleft,(350,350))
    cv2.imwrite('image_left.png',imgleft)
    photo=PhotoImage(file='image_left.png')
    
    canvasleft.delete("all")
    canvas2 = canvasleft.create_image(1,1,anchor=NW, image=photo)
    canvasleft.itemconfig(canvas1, image = canvas2)
    canvasleft.pack()
    leftframe.pack(side=LEFT)
    root.mainloop()
    
def browseimage_right():
    filename = fdialog.askopenfilename()
    imgright = cv2.imread(filename)
    imgright=cv2.resize(imgright,(350,350))
    cv2.imwrite('image_right.png',imgright)
    photo=PhotoImage(file='image_right.png')
    
    canvasright.delete("all")
    canvas2 = canvasright.create_image(1,1,anchor=NW, image=photo)
    canvasright.itemconfig(canvas1, image = canvas2)
    canvasright.pack()
    rightframe.pack(side=RIGHT)
    root.mainloop()
    
def panorama():
    stitch.stitch()
    final=cv2.imread('final.png')
    photo=PhotoImage(file='final.png')
    
    canvasleft.delete("all")
    canvasright.delete("all")
    canvas2 = canvasleft.create_image(1,1,anchor=NW, image=photo)
    canvasleft.itemconfig(canvas1, image = canvas2)
    canvasleft.pack()
    leftframe.pack(side=LEFT)
    root.mainloop()
            
#GUI
#Create window
root = Tk()
root.title("Face enabled Time clock")
root.geometry("910x550")

#Create topframe, bottomframe, leftframe and rightframe
topframe=Frame(root)
topframe.pack(side=TOP)

bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)

leftframe=Frame(topframe,bg='black')
leftframe.pack(side=LEFT)

rightframe=Frame(topframe)
rightframe.pack(side=RIGHT)

canvasleft=Canvas(leftframe,width=327,height=363)
canvasleft.pack()
photo=PhotoImage(file='upload_symbol.png')
canvas1=canvasleft.create_image(20,10,anchor=NW, image=photo)
leftframe.pack(side=LEFT)

canvasright=Canvas(rightframe,width=327,height=363)
canvasright.pack()
canvas1=canvasright.create_image(20,10,anchor=NW, image=photo)
rightframe.pack(side=RIGHT)
    
#buttons
Bt1=Button(bottomframe,text="Capture Left Image",background="LightBlue", bd=0,width=15,height=1,command=browseimage_left)
Bt1.pack(fill=X,pady=10)

Bt2=Button(bottomframe,text="Capture Right Image",background="LightBlue", bd=0,width=15,height=1,command=browseimage_right)
Bt2.pack(fill=X,pady=10)

Bt3=Button(bottomframe,text="Panorama",background="LightBlue", bd=0,width=15,height=1,command=panorama)
Bt3.pack(fill=X,pady=10)

Bt3=Button(bottomframe,text="Exit",background="LightBlue", bd=0,width=15,height=1,command=root.destroy)
Bt3.pack(fill=X,pady=10)

rightframe.pack(side=RIGHT)

#stable main window on infinity time
root.mainloop()
