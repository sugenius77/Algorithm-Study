import sys
from collections import deque

# 3. BFS 구현
def bfs(mid):
  visited[one] = 1
  q = deque([one])
  while q:
    now = q.popleft()
    if now == two:
      return True
    for nx, nc in graph[now]:
      if visited[nx] == 0 and mid <= nc:
        q.append(nx)
        visited[nx] = 1
  return False

# 1. 입력 받기
n,m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
  a,b,c = map(int,sys.stdin.readline().split())
  graph[a].append((b,c))
  graph[b].append((a,c))

# 공장 위치
one, two = map(int,sys.stdin.readline().split())

# 2. 이분탐색
# 이분탐색 전 정렬 필요  
for i in range(1, n + 1):
  graph[i].sort(reverse=True)
  
start,end = 1, 1000000000
# 이분 탐색으로 한번의 이동으로 옮길 수 있는 물품들의 중량의 최댓값 찾기
while start <= end:
  visited = [0 for _ in range(n + 1)]
  mid = (start + end) // 2
  if bfs(mid):
    start = mid + 1
  else:
    end = mid - 1
    
print(end)




