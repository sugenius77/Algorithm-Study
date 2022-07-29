import sys
from collections import deque

def bfs(n):
  q = deque([n])
  answer = 0
  visited[n]= True
  while q:
    v = q.popleft()
    for i in graph[v]:
      if not visited[i]:
        q.append(i)
        visited[i] = True
        answer += 1
  return answer
  
t = int(sys.stdin.readline())

for _ in range(t):
  n,m = map(int,sys.stdin.readline().split())
  graph = [[]*(m+1) for _ in range(n+1)]
  visited = [False] * (n+1)
  for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
  print(bfs(n))