# 시에르핀스키 삼각형

from tkinter import *

## 함수선언
def drawTraiangle(x, y, size):
    if size >= 30: 
        drawTraiangle(x, y, size/2) # 왼쪽 아래
        drawTraiangle(x+size/2, y, size/2) # 오른쪽 아래
        drawTraiangle(x+size/4, int(y-size*(3*0.5)/4), size/2) # 중심 위쪽
    
    else:
        canvas.create_polygon(x, y, x+size, y, x+size/2, y-size*(3**0.5)/2, fill='red', outline='red')

## 전역변수
wSize = 1000
radius = 400

## 메인코드
root = Tk()
root.title('시에르핀스키 삼각형')
canvas = Canvas(root, height=wSize, width=wSize, bg='white')

drawTraiangle(wSize/5, wSize/5*4, wSize*2/3)

canvas.pack()
root.mainloop()
