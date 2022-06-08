# 수빈이가 있는 위치,동생이 있는 위치
n, k = map(int,input().split())
dist = [0 for _ in range(100001)]

from collections import deque
def bfs(n):
  queue = deque([n])
  while queue:
    x = queue.popleft()
    if x == k:
      print(dist[x])
      break
    for i in (x-1, x+1,x*2):
      if 0 <= i <= 100000 and not dist[i]:
        dist[i] = dist[x] + 1
        queue.append(i)
        
bfs(n)