import sys

t = int(sys.stdin.readline())
for _ in range(t):
  cnt = 0
  x1, y1, x2, y2 = map(int,sys.stdin.readline().split())
  n = int(sys.stdin.readline())
  for i in range(n):
    cx, cy, r = map(int,sys.stdin.readline().split())
    # 두 점 사이의 거리
    dist1 = ((cx - x1) **2 + (cy - y1) **2) ** 0.5
    dist2 = ((cx - x2) **2 + (cy - y2) **2) ** 0.5
    if dist1 > r and dist2 < r:
      cnt += 1
    if dist2 > r and dist1 < r:
      cnt += 1
  print(cnt)