import sys
from collections import deque

# bfs 함수 밖에 정의
q = deque()

### 2
def bfs():
  # q.append((x,y))
  # 큐가 비워질때까지 반복문
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if  graph[nx][ny] == 0:
          graph[nx][ny] = graph[x][y]+1
          q.append((nx,ny))
  
### 1
# 가로 칸, 세로 칸
m,n = map(int,sys.stdin.readline().split())
graph = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# graph = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]]
for i in range(n):
  graph.append(list(map(int,sys.stdin.readline().split())))
# 익은 토마토의 좌표를 먼저 큐에 저장
for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      q.append((i,j))  

bfs()
cnt = 0
# graph = [[9, 8, 7, 6, 5, 4], [8, 7, 6, 5, 4, 3], [7, 6, 5, 4, 3, 2], [6, 5, 4, 3, 2, 1]]
for i in graph:
  for j in i:
    if j == 0:
      print(-1)
      exit(0)
  cnt = max(cnt,max(i))
#  처음을 1로 시작했으므로 -1을 빼줌
print(cnt-1)


