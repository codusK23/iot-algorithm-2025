import random
import time

def sortBubble(ary):
    n = len(ary)
    for end in range(n-1, 0, -1):
        changeYn = False
        for cur in range(0, end):
            if ary[cur] > ary[cur + 1]:
                ary[cur], ary[cur + 1] = ary[cur + 1], ary[cur]
                changeYn = True
        if not changeYn:
            break
    return ary

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

def sortQuick(ary):
    sortQuickN(ary, 0, len(ary)-1)

tempAry = [random.randint(10000, 99999) for _ in range(1000000)]
tempAry.sort()

rndPos = random.randint(0, len(tempAry)-1)
print(f'# 데이터 개수 -> ', len(tempAry))
print(f'# 끼어든 위치 -> ', rndPos)
tempAry.insert(rndPos, tempAry[-1])

bubbleAry = tempAry[:]
quickAry = tempAry[:]

start = time.time()
sortBubble(bubbleAry)
end = time.time()
print(f'다시 정렬 시간(퀵 정렬) -> {(end-start):>10.3f}초')

start = time.time()
sortQuick(quickAry)
end = time.time()
print(f'다시 정렬 시간(퀵 정렬) -> {(end-start):>10.3f}초')