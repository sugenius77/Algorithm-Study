import sys
from collections import deque

# 행,열
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# 그림의 개수
num = 0

# 가장 큰 그림 = 1의 개수가 많은 것
max_cnt = 0

dx = [0, 1, -1, 0]  
dy = [1, 0, 0, -1]

# bfs 구현
def bfs(x, y):
    q = deque()
    q.append([x, y])
    # 1을 세주는 cnt
    cnt = 1
    visited[x][y] = True
    while q:
      x, y = q.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
          if not visited[nx][ny] and graph[nx][ny] == 1:
            q.append([nx, ny])
            visited[nx][ny] = True
            cnt += 1  
    return cnt
  

for i in range(n):
  for j in range(m):
    # 값이 1이고 방문하지 않았다면
    if graph[i][j] == 1 and not visited[i][j]:
      num += 1     
      max_cnt = max(max_cnt,bfs(i,j))
      
print(num)    
print(max_cnt)
