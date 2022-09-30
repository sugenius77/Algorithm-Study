import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
graph = []

for _ in range(n):
  graph.append(list(map(int,sys.stdin.readline().strip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(x,y):
  q = deque([(x,y)])
  graph[x][y] =  1
  while q:
    a,b = q.popleft()
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if graph[nx][ny] == 1:
          q.append([nx,ny])
          graph[nx][ny] = graph[a][b] + 1

bfs(0,0)
print(graph[n-1][m-1])
