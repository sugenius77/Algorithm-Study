import sys
length = int(sys.stdin.readline())
note = list(sys.stdin.readline().rstrip())

# 동남서북(idx: 0,1,2,3)쪽으로 한 칸 가는 좌표
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 초기 위치는 0,0 바라보는 방향은 남쪽(1)
x,y,direction= 0,0,1
graph = [[x,y]]

for i in note:
  if i == 'R':
    direction = (direction + 1) % 4
  if i == 'L':
    direction = (direction - 1) % 4
  if i == 'F':
    x = x + dx[direction]
    y = y + dy[direction]
    graph.append([x,y])

# 행    
n = max(graph)[0] - min(graph)[0] + 1

# 열
m = max(graph, key = lambda x:x[1])[1] - min(graph, key = lambda x:x[1])[1] + 1

min_x = min(graph, key = lambda x:x[0])[0] 
min_y = min(graph, key = lambda x:x[1])[1]

for i in graph:
  i[0] = i[0] + abs(min_x)
  i[1] = i[1] + abs(min_y)


# 이중배열 선언 
map =  [[False] *m for _ in range(n)]

for i in graph:
  if map[i[0]][i[1]] == False:
    map[i[0]][i[1]] = '.'

for i in map:
  for j in range(m):
    if i[j] == False:
      i[j] = '#'

for i in map:
  for j in range(len(i)):
    print(i[j],end="")
  print("")