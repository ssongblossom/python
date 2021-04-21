import myTurtle
import turtle
import random
from tkinter.simpledialog import * 

tX, tY, tColor, tSize = [None] * 4     
swidth, sheight=500, 500

if __name__ == "__main__":
    swidth, sheight=500, 500
    turtle.title('거북 모듈 활용')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)
    turtle.shape("turtle")

    inStr = myTurtle.getString()
    turtle.penup()

    for ch in inStr:
        colorList = []
        colorList = myTurtle.getColor()
        xyList = []
        xyList = myTurtle.getXY(swidth,sheight)
        tSize = myTurtle.getTextSize()
        turtle.goto(xyList[0],xyList[1])
        turtle.color(colorList[0],colorList[1],colorList[2])
        turtle.write(ch, move=False, align="left", font=("Arial", tSize, "normal"))




