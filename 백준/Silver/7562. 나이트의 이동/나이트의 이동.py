import sys
from collections import deque

### 2. 함수 정의
def bfs(x,y,tx,ty):
    q = deque()
    # 큐에 시작 위치 넣고
    q.append((x, y))
    # 방문 표시
    graph[x][y] = 1
    while q:
        x,y = q.popleft()
        # for문 바깥쪽에서 체크
        if x == tx and y == ty:
            return print(graph[tx][ty]-1)
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l:
                if graph[nx][ny] == 0:
                    q.append((nx,ny))
                    graph[nx][ny] = graph[x][y] + 1
                    

### 1. 입력
t = int(sys.stdin.readline())

# 이동 방향
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

for i in range(t):
    l = int(sys.stdin.readline())
    # lxl 체스판
    graph = [[0] * l for _ in range(l)]
    # 시작 위치
    x, y = map(int,sys.stdin.readline().split())
    # 목표 위치: target x,y
    tx, ty = map(int,sys.stdin.readline().split())
    bfs(x,y,tx,ty)





