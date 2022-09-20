import sys
import copy
from collections import deque
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
# 모든 섬을 포함하는 가장 작은 직사각형으로 지도의 크기 자르기
  answer = []
  # for i in result:
  #   # print(i)
  #   if 'X' in i:
  #     print(i)
  #     answer.append(i)
  # # print(answer)
  # # # 필요없는 영역 자르기
  # # result = deque(result)
  # # while( 'X' not in result[0] ):
  # #     result.popleft()
  # # while( 'X' not in result[-1]):
  # #     result.pop()
  # # print(result)

  # start = 0
  # end = len(result[0]) - 1
  
  # # 플래그 이용
  # # 50년 후 지도 시작 부분
  # flag = True
  # while flag:
  #   for i in result:
  #     if i[start] == 'X':
  #       flag = False
  #       break
  #   else:
  #     start += 1
        
  # # 50년 후 지도 끝나는 부분
  # flag = True  
  # while flag:
  #   for i in result:
  #     if i[end] == 'X':
  #       flag = False
  #       break 
  #   else:  
  #     end  -= 1
  
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
  #   print(''.join(i[start:end+1]))
