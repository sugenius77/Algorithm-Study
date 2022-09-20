import sys
import copy

R, C = map(int,sys.stdin.readline().split())
graph = []

for _ in range(R):
  graph.append(list(sys.stdin.readline().strip()))

result = copy.deepcopy(graph)
land_cnt = 0
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for i in range(R):
  for j in range(C):
    if graph[i][j] =='X':
      cnt = 0
      land_cnt += 1
      for z in range(4):
        nx = i + dx[z]
        ny = j + dy[z]
        # 모서리에 섬이 있을 때
        # 인접한 칸은 범위 밖으로 넘어가며 바다라고 취급하여 카운트한다.
        if 0 > nx or nx >= R or 0 > ny or ny >= C:
          cnt += 1
        # 모서리가 아닌 부분에 섬이 있을 때
        # 0 <= nx < R and 0 <= ny <= C
        elif graph[nx][ny] == '.':
          cnt += 1
      if cnt >= 3:
        result[i][j] = '.'
        land_cnt -= 1
        
if land_cnt == 0:
  print('X')
else:
  startR = 0
  endR = 0
  for i in range(R):
    if 'X' in result[i]:
      startR = i
      break
  for i in range(R-1,-1,-1):
    if 'X' in result[i]:
      endR = i
      break
  
  idx = []
  for j in range(C):
    for i in range(startR, endR + 1):
      if 'X' == result[i][j]:
        idx.append(j)
        break

  for i in result[startR:endR+1]:
    print(''.join(i[idx[0]:idx[-1]+1]))
  
