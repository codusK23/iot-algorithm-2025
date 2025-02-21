# 이미지 처리(정렬 알고리즘)

from tkinter import *

def sortQuickN(ary, start, end):
    if end <= start: return

    low = start; high = end

    pivot = ary[(low + high) // 2] 
    while low <= high:
        while ary[low] < pivot:
            low += 1
        while ary[high] > pivot:
            high -= 1
        if low <= high:
            ary[low], ary[high] = ary[high], ary[low]
            low, high = low + 1, high -1

    sortQuickN(ary, start, low-1) 
    sortQuickN(ary, low, end)

root = Tk()
root.geometry('600x600')
root.title('이미지처리(정렬)')

photo = PhotoImage(file='image/cupdog.png')

photoAry = []
h = photo.height() # 600
w = photo.width() # 600
for i in range(h): # 행렬 row와 동일
    for k in range(w): # 행렬 col와 동일
        r, g, b = photo.get(i, k)
        value = (r + g + b) // 3 # 평균치
        photoAry.append(value)

print(len(photoAry)) # 360000 리스트가 생성

# 퀵소트로 정렬
dataAry = photoAry[:]
sortQuickN(dataAry, 0, len(dataAry)-1)
midvalue = dataAry[h*w // 2]

# 색상들을 정리. 127보다 작으면 검은색, 127보다 크면 흰색
for i in range(len(photoAry)):
    if photoAry[i] <=midvalue:
        photoAry[i] = 0 # black
    else:
        photoAry[i] = 255 # white

# 흑백이미지로 변경
pos = 0
for i in range(h):
    for k in range(w):
        r = g = b = photoAry[pos]
        pos += 1
        photo.put(f'#{r:02x}{g:02x}{b:02x}', (i, k)) # photo에 각 위치의 색상을 photoAry에 들어있는 값으로 변경

paper = Label(root, image=photo)
paper.pack(expand=1, anchor=CENTER)

root.mainloop()
