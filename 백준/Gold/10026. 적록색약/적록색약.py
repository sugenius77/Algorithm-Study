
import sys
n = int(sys.stdin.readline())
sys.setrecursionlimit(1000000)
graph = []
for i in range(n):
  graph.append(list(sys.stdin.readline().rstrip()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
three_cnt = 0
two_cnt = 0

def dfs(x,y,color):
  visited[x][y] = True
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < n:
      if not visited[nx][ny] and graph[nx][ny] == color:
        visited[nx][ny] = True
        dfs(nx,ny,color)

# 적록색약이 아닌 사람이 봤을 때 구역의 개수
visited = [[False] * n for _ in range(n)]        
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      dfs(i,j,graph[i][j])
      three_cnt += 1

# 그래프 바꿔기 (R -> G)
for i in range(n):
  for j in range(n):
    if graph[i][j] == 'R':
      graph[i][j] = 'G'

# 적록색약인 사람이 봤을 때 구역의 개수
visited = [[False] * n for _ in range(n)]        
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      dfs(i,j,graph[i][j])
      two_cnt += 1
      
print(three_cnt, two_cnt)
