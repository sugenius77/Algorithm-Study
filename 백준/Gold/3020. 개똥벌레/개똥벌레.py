import sys
# 동굴의 길이와 높이
n, h = map(int, sys.stdin.readline().split())

# 석순
down = [0] * (h+1)
# 종유석
up = [0] * (h+1)

for i in range(n):
  # 석순
  if i % 2 == 0:
    down[int(sys.stdin.readline())] += 1
  # 종유석
  else:
    up[int(sys.stdin.readline())] += 1

for i in range(h-1,0,-1):
  down[i] += down[i+1]
  up[i] += up[i+1]

# 파괴해야하는 장애물의 최소값
min_cnt = n
# 최소값이 나타나는 구간의 수
range_cnt = 0

for i in range(1,h+1):
  if min_cnt > (down[i]+up[h-i+1]):
    min_cnt = down[i]+up[h-i+1]
    range_cnt = 1
  elif min_cnt == down[i]+up[h-i+1]:
    range_cnt += 1

print(min_cnt,range_cnt)

