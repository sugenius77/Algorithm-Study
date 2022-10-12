import sys

r,c = map(int,sys.stdin.readline().split())
graph = []

for _ in range(r):
  graph.append(list(sys.stdin.readline().strip()))

dx = [-1,1,0,0]
dy = [0,0,1,-1]
# visited = [[False] * c for _ in range(r)]
alpha = set()
ans = 0

def dfs(x,y,cnt):
  global ans
  ans = max(ans, cnt)
  # visited[x][y] = True
  alpha.add(graph[x][y])
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < r  and 0 <= ny < c:
      # if not visited[nx][ny]:
        if graph[nx][ny] not in alpha:
          # visited[nx][ny] = True
          dfs(nx,ny,cnt+1)
          # visited[nx][ny] = False
          alpha.remove(graph[nx][ny])
          

dfs(0,0,1)
print(ans)