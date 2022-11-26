import sys
from collections import deque 
n,m = map(int,sys.stdin.readline().split())

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (n+1)
student = [[] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int,sys.stdin.readline().split())
  student[a].append(b)
  # 진입차수 1 증가
  indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
  result = []
  q = deque()
  for i in range(1, n+1):
    if indegree[i] == 0:
      q.append(i)
  while q:
    now = q.popleft()
    result.append(now)
    for i in student[now]:
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)
  for i in result:
    print(i, end=" ")
topology_sort()






