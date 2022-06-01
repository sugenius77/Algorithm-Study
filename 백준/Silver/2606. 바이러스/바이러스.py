import sys

n = int(sys.stdin.readline())

num = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count = 0

for i in range(num):
  a,b = map(int,sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

# DFS 구현
def dfs(graph,v,visited):
  global count
  visited[v] = True
  for i in graph[v]:
    if not visited[i]:
      count += 1
      dfs(graph,i,visited)
      
# 웜이 감염된 컴퓨터의 갯수 구하기
for i in range(1,n+1):
  if visited[i] == False:
    dfs(graph,i,visited)
    break
    
print(count)
  