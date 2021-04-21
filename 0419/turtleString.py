import turtle
import random
from tkinter.simpledialog import * 

tX, tY, tColor, tSize = [None] * 4     # 거북 2차원 리스트
swidth, sheight=500, 500

## 메인 코드 부분 ##
if __name__ == "__main__" :
     turtle.title('거북 리스트 활용')
     turtle.setup(width = swidth + 50, height = sheight + 50)
     turtle.screensize(swidth, sheight)
     turtle.shape("turtle")

     inStr = askstring('문자열 입력', '거북이 쓸 문자열을 입력')

     for ch in inStr:
          turtle.penup()
          tX = random.randrange(-swidth / 2, swidth / 2)
          tY = random.randrange(-sheight / 2, sheight / 2)
          tSize = random.randrange(10, 50)
          r = random.random(); g = random.random(); b = random.random()
          turtle.goto(tX,tY)
          turtle.pencolor(r,g,b)
          turtle.write(ch, move=False, align="left", font=("Arial", tSize, "normal"))
          
turtle.done()