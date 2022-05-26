import sys
from collections import deque

### 입력 받기
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

# 상하좌우
dx = [1,-1,0,0]
dy = [0,0,1,-1]
x,y,shark_size = 0,0,2

# 아기 상어가 먹은 물고기
eat = 0

# 아기 상어 위치
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x = i
            y = j
# 아기 상어가 있는 위치의 값 = 0          
graph[x][y] = 0

# 아기 상어보다 작은 물고기가 있는지 확인하면 존재한다면 가장 가까운 애들부터 먹는다.
def bfs(x,y,shark_size):
    visited = [[0] * n for _ in range(n)]
    q = deque()
    q.append((x,y,0))
    visited[x][y] = 1
    # 그 물고기까지의 이동 거리, 물고기 행과 열
    fish = []
    while q:
        x,y,dist = q.popleft()
        # 상하좌우 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 좌표 값이 유효하고, 방문한 적이 없다면
            if 0<= nx < n and 0<= ny < n and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                # 물고기가 아기 상어보다 작다면
                if graph[nx][ny] != 0 and graph[nx][ny] < shark_size:
                  fish.append((dist+1,nx,ny))
                  q.append((nx,ny, dist+1))
                  visited[nx][ny] = 1
                elif graph[nx][ny] == 0 or graph[nx][ny] == shark_size:
                  visited[nx][ny] = 1
                  q.append((nx,ny,dist+1))

    fish.sort()
    if fish:
      # 최단 거리의 물고기 - 행이 가장 작은 위치 - 열이 가장 작은 위치
      return [fish[0][1],fish[0][2],fish[0][0]]
    else:
      return []

# 이동 거리
result = 0
while 1:
    bite_fish = bfs(x,y,shark_size)
    if bite_fish:
        a, b, move = bite_fish
        graph[x][y] = 0
        eat += 1
        result += move
        # 아기 상어가 먹은 물고기의 수 = 아기상어의 현재 크기
        if eat == shark_size:
            shark_size += 1
            eat = 0
        x,y = a, b
    # 더 이상 먹을 물고기가 없다면
    else:
        break
 

print(result)


