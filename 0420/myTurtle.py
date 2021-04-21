import random
from tkinter.simpledialog import * 

def getString():
     inStr = askstring('문자열 입력', '거북이 쓸 문자열을 입력')
     return inStr

def getColor():
     colorList = []
     for i in range(0,3):
          colorList.append(random.random())
     return colorList

def getXY(swidth,sheight):
     tX = random.randrange(-swidth / 2, swidth / 2)
     tY = random.randrange(-sheight / 2, sheight / 2)
     xyList = []
     xyList.append(tX); xyList.append(tY)
     return xyList

def getTextSize():
     return random.randrange(10, 50)