import sys

r,c = map(int,sys.stdin.readline().split())
graph = []

for _ in range(r):
  graph.append(list(sys.stdin.readline().strip()))

dx = [-1,1,0,0]
dy = [0,0,1,-1]
alpha = set()
ans = 0

def dfs(x,y,cnt):
  global ans
  ans = max(ans, cnt)
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < r  and 0 <= ny < c:
      if graph[nx][ny] not in alpha:
        alpha.add(graph[nx][ny])
        dfs(nx,ny,cnt+1)
        alpha.remove(graph[nx][ny])
          
alpha.add(graph[0][0])
dfs(0,0,1)

print(ans)