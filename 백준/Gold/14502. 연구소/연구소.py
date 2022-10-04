import sys
from collections import deque
import copy

n,m = map(int,sys.stdin.readline().split())

graph = []
for i in range(n):
  graph.append(list(map(int,sys.stdin.readline().split())))


dx = [-1,1,0,0]
dy = [0,0,-1,1]
q = deque()
ans = 0

def bfs():
  global ans
  tmp = copy.deepcopy(graph)
  # 2인 곳에서 바이러스 퍼지기 시작
  for i in range(n):
    for j in range(m):
      if tmp[i][j] == 2:
        q.append([i,j])
  # 상하좌우가 0이라면 2로 바꾸기 = 바이러스 퍼지는 중
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if tmp[nx][ny] == 0:
          tmp[nx][ny] = 2
          q.append([nx,ny])
  # 0의 개수 세기
  cnt = 0
  for i in tmp:
    cnt += i.count(0)
  ans = max(cnt,ans)

# 백트래킹을 이용해서 벽을 세우는 경우의 수 구하기
def make_wall(x):
  if x == 3:
    bfs()
    return 
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        graph[i][j] = 1
        make_wall(x+1)
        graph[i][j] = 0

make_wall(0)
print(ans)