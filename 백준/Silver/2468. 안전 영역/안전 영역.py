import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
board = []

for _ in range(n):
  board.append(list(map(int,sys.stdin.readline().split())))

min_h = min(map(min, board))
max_h = max(map(max, board))
   
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,h):
  visited[x][y] = True
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < n:
      if not visited[nx][ny] and board[nx][ny] > h: 
        visited[nx][ny] = True
        dfs(nx,ny,h)

max_cnt = 0
for h in range(min_h-1,max_h):
  visited = [[False] *n for _ in range(n)]
  cnt = 0
  for i in range(n):
    for j in range(n):
      if not visited[i][j] and board[i][j] > h:  
        dfs(i,j,h)
        cnt += 1
  if max_cnt < cnt:
    max_cnt = cnt

print(max_cnt)