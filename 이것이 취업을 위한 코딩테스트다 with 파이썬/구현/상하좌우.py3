import sys

N = int(sys.stdin.readline())
map = list(sys.stdin.readline().split())
x,y = 1,1

# 상,하,좌,우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
move_type = ['U','D','L','R']

# 이동 방향을 하나씩 확인
for i in map:
  # 이동 후 좌표 구하기
  for j in range(len(move_type)):
    if i == move_type[j]:
      nx = x + dx[j]
      ny = y + dy[j]
  # 공간을 벗어나는 경우 무시
  if 1 > nx or nx > N or ny < 1 or ny > N:
    continue
  x,y = nx,ny

print(x,y)
