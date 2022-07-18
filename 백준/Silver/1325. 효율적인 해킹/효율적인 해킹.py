import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())


def bfs(start):
  cnt = 1
  visited = [False] * (n+1)
  q = deque([start])
  visited[start] = True
  while q:
    v = q.popleft()
    for i in graph[v]:
      if not visited[i]:
        q.append(i)
        visited[i] = True
        cnt += 1
  return cnt
  
graph = [[] for i in range(n+1)]
for _ in range(m):
  a,b = map(int,sys.stdin.readline().split())
  graph[b].append(a)  
  
result = []
max_num = 1
for i in range(1,n+1):
  cnt = bfs(i) 
  if max_num < cnt:
    max_num = cnt
    result.clear()
    result.append(i)
  elif max_num == cnt:
    result.append(i)
    

print(*result)


