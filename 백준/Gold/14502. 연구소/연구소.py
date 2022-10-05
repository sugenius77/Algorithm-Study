import sys
from collections import deque
from itertools import combinations
import copy

n,m = map(int,sys.stdin.readline().split())

graph = []
virus_zone = []
safe_zone = []
for i in range(n):
  graph.append(list(map(int,sys.stdin.readline().split())))


dx = [-1,1,0,0]
dy = [0,0,-1,1]

ans = 0

# 벽을 3개 세울 때 중복되는 조합 없게 하기 위해 combination 사용
# ex) (1,1) (2,4) (3,5) 세우고 검사한 뒤 나중에 (2,4) (1,1) (3,5)를 방지하기 위해
for i in range(n):
  for j in range(m):
    if graph[i][j] == 2:
      virus_zone.append([i,j])
    if graph[i][j] == 0:
      safe_zone.append([i,j])


def bfs(tmp_graph):
  global ans
  q = deque(virus_zone)

  # 상하좌우가 0이라면 2로 바꾸기 = 바이러스 퍼지는 중
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if tmp_graph[nx][ny] == 0:
          tmp_graph[nx][ny] = 2
          q.append([nx,ny])
  # 0의 개수 세기
  cnt = 0
  for i in tmp_graph:
    cnt += i.count(0)
  ans = max(cnt,ans)

# 조합을 이용해서 경우의 수 구하기
def make_wall():
  safe_zones_combi = combinations(safe_zone, 3)
  
  for walls in safe_zones_combi:
      a, b, c = walls[0], walls[1], walls[2]

      graph[a[0]][a[1]] = 1
      graph[b[0]][b[1]] = 1
      graph[c[0]][c[1]] = 1

      tmp_graph = [item[:] for item in graph]

      bfs(tmp_graph)

      graph[a[0]][a[1]] = 0
      graph[b[0]][b[1]] = 0
      graph[c[0]][c[1]] = 0

make_wall()
print(ans)