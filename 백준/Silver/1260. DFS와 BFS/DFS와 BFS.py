import sys
from collections import deque


def dfs(v):
  visited[v] = True
  print(v, end = " ")
  for i in graph[v]:
    if not visited[i]:
      dfs(i)

def bfs(v,n):
  q = deque([v])
  visited = [False] * (n+1)
  visited[v] = True
  while q:
    v = q.popleft()
    print(v, end =" ")
    for i in graph[v]:
      if not visited[i]:
        q.append(i)
        visited[i] = True
        
n,m,v = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
  a,b = map(int,sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)
for i in range(len(graph)):
  graph[i] = sorted(graph[i])


dfs(v)
print("")
bfs(v,n)