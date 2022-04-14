##### 실행 순서 1
import sys
# 재귀 limit 설정
sys.setrecursionlimit(10000)

# 지도의 크기
n = int(sys.stdin.readline())

# 지도
graph = [[] for i in range(n)]
for i in range(n):
  graph[i] = list(map(int,sys.stdin.readline().rstrip()))
 
# 총 단지수
apt = []
# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

### 실행 순서 3
def dfs(x,y):
  global cnt
  # 방문 처리
  graph[x][y] = 0
  # 단지 내 집의 수 증가
  cnt += 1
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < n:
      if graph[nx][ny] == 1:
        dfs(nx,ny)
        
### 실행 순서 2: 입력 받고 입력 받은 값들로 for문을 돈다.
# garph[0][0] ~ graph[n][n]     
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      # 각 단지 내 집의 수
      cnt = 0
      dfs(i, j)
      # 단지 내 집의 갯수 다 세고 나와서, 단지 갯수 추가
      apt.append(cnt)

# 총 단지 수 출력
print(len(apt))
# 단지 정렬
apt.sort()
# 단지 갯수 출력
for i in apt:
  print(i)

