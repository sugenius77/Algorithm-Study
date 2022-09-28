import sys

n = int(sys.stdin.readline())

graph = []
start = []
link = []

for _ in range(n):
  graph.append(list(map(int,sys.stdin.readline().split())))

# 1000000000
min_diff = int(1e9)

def dfs(index):
  global min_diff
  # 재귀 탈출 조건 = 백트래킹 탑 체크 시점
  if index == n//2:
    Spower,Lpower = 0,0
    # 스타트팀에 없으면 링크팀에 넣기
    for i in range(n):
      if i not in start:
        link.append(i)
    # 각 팀의 능력치 구하기
    for i in range(n//2-1):
      for j in range(i+1,n//2):
        Spower += graph[start[i]][start[j]] + graph[start[j]][start[i]]
        Lpower += graph[link[i]][link[j]] + graph[link[j]][link[i]]
    diff = abs(Spower-Lpower)
    
    # 능력치가 최소인지 확인
    if min_diff > diff:
      min_diff = diff
    # 링크팀은 계산이 끝나면 항상 비워준다.
    link.clear()
    return
  
  # dfs
  for i in range(n):
    if i in start:
      continue
    if len(start) > 0 and start[len(start)-1] > i:
      continue
    start.append(i)
    dfs(index+1)
    start.pop()


dfs(0)
print(min_diff)
