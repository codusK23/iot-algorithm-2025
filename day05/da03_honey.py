class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

# 전역변수
G1 = None
storeAry = [['GS25', 30], ['CU', 60], ['Seven11', 10], ['MiniStop', 90], ['Emart24', 40]]
GS25, CU, Seven11, Ministop, Emart24 = 0, 1, 2, 3, 4

def printGraph(g):
    global storeAry
    
    print('', end='\t')
    for v in range(g.SIZE):
        print(f'{storeAry[v][0]:>9s}', end='\t')
    print()

    for row in range(g.SIZE):
        print(f'{storeAry[row][0]:>9s}', end='') 
        for col in range(g.SIZE):
            print(f'{g.graph[row][col]:>8d}', end='\t')
        print()
    print()

# 메인코드
gSize = 5
G1 = Graph(gSize)
G1.graph[GS25][CU] = 1; G1.graph[GS25][Seven11] = 1
G1.graph[CU][GS25] = 1; G1.graph[CU][Seven11] = 1; G1.graph[CU][Ministop] = 1
G1.graph[Seven11][GS25] = 1; G1.graph[Seven11][CU] = 1; G1.graph[Seven11][Ministop] = 1
G1.graph[Ministop][Seven11] = 1; G1.graph[Ministop][CU] = 1; G1.graph[Ministop][Emart24] = 1
G1.graph[Emart24][Ministop] = 1

print("## 편의점 그래프 ##")
printGraph(G1)

stack = []
visitedAry = [] # 방문한 편의점

current = 0                         # 시작 편의점
maxStore = current                  # 최대 개수 편의점 번호 (GS25)
maxCount = storeAry[current][1]     # 편의점에 있는 허니버터 숫자
stack.append(current)
visitedAry.append(current)

while len(stack) != 0:
    next = None
    for vertex in range(gSize):
        if G1.graph[current][vertex] == 1:
            if vertex in visitedAry:        # 방문한 적이 있는 편의점이면 탈락
                continue
            else:                           # 방문한 적 없는 편의점이면 다음 편의점으로 지정
                next = vertex
                break

    if next != None:            # 방문할 다음 편의점이 있는 경우
        current = next
        stack.append(current)
        visitedAry.append(current)
        if storeAry[current][1] > maxCount:
            maxCount = storeAry[current][1]
            maxStore = current
    
    else:                   # 방문할 다음 편의점이 없는 경우
        current = stack.pop()

print(f'허니버터칩 최대 보유 편의점(개수)--> {storeAry[maxStore][0]} ({storeAry[maxStore][1]})')