from tkinter import *
import random
from tkinter import messagebox


## 변수 선언 부분 ##
btnList = [""] * 8
fnameList = ["icecream.gif", "jellybean.gif", "kitkat.gif", "lollipop.gif", "marshmallow.gif", "nougat.gif", "oreo.gif", "pie.gif"]
photoList=[None] * 8
i, k = 0, 0


xPos, yPos = 0, 0
isEmpty = False
num = 0
emptyIndex = [2,2]
posList = []
pos = []

def buttonClick():
    pass

## 메인 코드 부분 ##
window = Tk()
window.geometry("210x210")

label = Label(window, text = str(random.randrange(0,10)), font = ("",200),width = 210, height = 210)
label.pack()


for i in range(0, 8) :
    photoList[i] = PhotoImage(file = "gif/" + fnameList[i])
    btnList[i] = Button(window, image = photoList[i], command = buttonClick)
    

for i in range(0, 3) :
    for k in range(0, 3) :
        if i!=emptyIndex[0] or k!=emptyIndex[1] :
            btnList[num].place(x = xPos, y = yPos)
            isEmpty = False
        else : 
            isEmpty = True
        num += 1
        xPos += 70
        pos.append(xPos)
        pos.append(yPos)
        pos.append(isEmpty)
        pos.append(num)
        posList.append(pos)
    xPos = 0
    yPos += 70




window.mainloop()