import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
board = [[] for _ in range(n)]

for i in range(n):
  board[i] = list(map(int,sys.stdin.readline().split()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
  q = deque([(0,0)])
  visited = [[False] * m for _ in range(n)]
  visited[0][0] = True
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if not visited[nx][ny]:
          if board[nx][ny] >= 1:
            board[nx][ny] += 1          
          else:
            visited[nx][ny] = True
            q.append([nx,ny])
       
t = 0
while True:
  bfs()
  flag = True
  for i in range(n):
    for j in range(m):
      if board[i][j] >= 3:
        board[i][j] = 0
        flag = False
      elif board[i][j] == 2:
        board[i][j] = 1
  if not flag:
    t += 1
  else:
    break

print(t)