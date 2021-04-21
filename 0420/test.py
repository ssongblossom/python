from tkinter import *
import random
from tkinter import messagebox

def imgbtn():
    btnList = [""] * 16
    fnameList = ["honeycomb.gif", "icecream.gif", "jellybean.gif", "kitkat.gif", "lollipop.gif", "marshmallow.gif", "nougat.gif", "oreo.gif"] * 2
    photoList=[None] * 16
    i, k,c = 0, 0,0
    xPos, yPos = 0, 0

    window = Tk()
    window.geometry("280x280")

    list =[]
    randloto= random.randint(0,15)
    for i in range(0,16,1):
        while randloto in list:
            randloto = random.randint(0,15)
        list.append(randloto)
                
    for i in range(0, 16) :
        photoList[i] = PhotoImage(file = "gif/" + fnameList[i])
        btnList[i] = Button(window, image = photoList[i] )  
        
    for i in range(0, 4) :
        for k in range(0, 4) :
            num = list[c]
            print(num)
            btnList[num].place(x = xPos, y = yPos)
            c+=1
            xPos += 70
        xPos = 0
        yPos += 70

    window.mainloop()
    
imgbtn()