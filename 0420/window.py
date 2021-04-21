from tkinter import *
from tkinter import messagebox

## 함수 선언 부분 ##
def clickLeft(event) :
    messagebox.showinfo("마우스", "마우스 왼쪽 버튼이 클릭됨")
def clickRight(event) :
    messagebox.showinfo("마우스", "마우스 오른쪽 버튼 클릭됨")
def clickMiddle(event) :
    messagebox.showinfo("마우스", "마우스 가운데 버튼 클릭됨")

def releaseLeft(event) :
    messagebox.showinfo("마우스", "마우스 왼쪽 버튼 떼어짐")
def releaseMiddle(event) :
    messagebox.showinfo("마우스", "마우스 가운데 버튼 떼어짐")
def releaseRight(event) :
    messagebox.showinfo("마우스", "마우스 오른쪽 버튼 떼어짐")

def doubleClickedLeft(event):
    messagebox.showinfo("마우스", "왼쪽 마우스 더블 클릭")
def doubleClickedMiddle(event):
    messagebox.showinfo("마우스", "가운데 마우스 더블 클릭")
def doubleClickedRight(event):
    messagebox.showinfo("마우스", "오른쪽 마우스 더블 클릭")

def dragLeft(event):
    messagebox.showinfo("마우스", "왼쪽 마우스 드래그")
def dragMiddle(event):
    messagebox.showinfo("마우스", "가운데 마우스 드래그")
def dragRight(event):
    messagebox.showinfo("마우스", "오른쪽 마우스 드래그")

def cursorIn(event):
    messagebox.showinfo("마우스", "마우스 IN")
    return True

def cursorOut(event):
    messagebox.showinfo("마우스", "마우스 OUT")
    return False

## 메인 코드 부분 ##

window = Tk()
""" double click보다 click이 우선으로 발생
window.bind("<Button-1>", clickLeft)
window.bind("<Button-2>", clickMiddle)
window.bind("<Button-3>", clickRight)
window.bind("<ButtonRelease-1>", releaseLeft)
window.bind("<ButtonRelease-2>", releaseMiddle)
window.bind("<ButtonRelease-3>", releaseRight)
"""
window.bind("<Double-Button-1>", doubleClickedLeft)
window.bind("<Double-Button-2>", doubleClickedMiddle)
window.bind("<Double-Button-3>", doubleClickedRight)

window.bind("<B1-Motion>", dragLeft)
window.bind("<B2-Motion>", dragMiddle)
window.bind("<B3-Motion>", dragRight)

button = Button(window, text = "Button")
button.pack()

#button.bind("<Enter>", cursorIn)  //enter와 leave를 같이 사용할 경우 enter와 동시에 leave
button.bind("<Leave>", cursorOut)






window.mainloop()