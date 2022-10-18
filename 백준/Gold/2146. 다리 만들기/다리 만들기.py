import sys
from collections import deque

n = int(sys.stdin.readline())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
count = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 섬의 개수를 세어주는 BFS
def count_bfs(x,y):
  global count
  q = deque()
  q.append([x,y])
  visited[x][y] = True
  board[x][y] = count

  while q:
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n:
        if board[nx][ny] == 1 and not visited[nx][ny]:
          board[nx][ny] = count
          visited[nx][ny] = True
          q.append([nx,ny])

answer = 1e9
# 바다를 건너며 가장 짧은 거리를 구하는 BFS
def dist_bfs(v):
  global answer
  dist = [[-1]*n for _ in range(n)]
  q = deque()
  for i in range(n):
    for j in range(n):
      if board[i][j] == v:
        q.append([i,j])
        dist[i][j] = 0
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n:
        # 다른 땅을 만나면 기존 답과 비교하여 짧은 거리 선택
        if board[nx][ny] > 0 and board[nx][ny] != v:
          answer = min(answer, dist[x][y])
          return 
        # 바다를 만나면 dist를 1씩 늘린다.
        if board[nx][ny] == 0 and dist[nx][ny] == -1:
          dist[nx][ny] = dist[x][y] + 1
          q.append([nx,ny])
        

for i in range(n):
  for j in range(n):
    if not visited[i][j] and board[i][j] == 1:
      count_bfs(i,j)
      count += 1

for i in range(1, count):
  dist_bfs(i)

print(answer)