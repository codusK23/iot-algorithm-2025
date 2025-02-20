from tkinter import *
import random

# 전역변수
colors = ['red', 'green', 'blue', 'black', 'orange', 'indigo', 'violet']
wSize = 1000
radius = 400


root=Tk()
root.title('원 모양의 프랙탈')

# 윈도우 창을 다 덮음 -> 그림을 그림(캔버스 밖으로는 못 그림)
canvas = Canvas(root, width=wSize, height=wSize, bg='white')
canvas.pack()


# 2. 프랙탈 원그리기 재귀함수 선언
def drawCircle(x, y, r):
    canvas.create_oval(x-r, y-r, x+r, y+r, width=2, outline=random.choice(colors))
    if r >= 5:
        drawCircle(x-r//2, y, r//2) # 중심의 왼쪽을 계속 그려감(재귀호출)
        drawCircle(x+r//2, y, r//2) # 중심의 오른쪽을 계속 그림


drawCircle(wSize//2, wSize//2, radius)
root.mainloop()
