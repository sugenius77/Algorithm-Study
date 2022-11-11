import sys
from itertools import combinations

n,m = map(int,sys.stdin.readline().split())

map = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

# 모든 집의 치킨 거리의 합 = 도시의 치킨 거리 -> 최소값을 구하기
ans  = int(1e9)

# 도시의 치킨 거리 최소값 구하기
def solve():
  global ans
  # 남겨둘 치킨 집의 조합
  for c in combinations(chicken,m):
    # 각 집에서의 치킨 거리를 합한 것
    chicken_total_dist = 0
    # 각 집에서의 치킨 거리
    for h in house:
      chicken_dist = int(1e9)
      # 집 하나랑 모든 치킨 집의 거리를 구해서 가장 작은 값을 구한다.
      for i in range(m):
        chicken_dist = min(chicken_dist, abs(h[0] - c[i][0]) + abs(h[1] - c[i][1]))
      chicken_total_dist += chicken_dist
    ans = min(chicken_total_dist,ans)

chicken = []
house = []

for i in range(n):
  for j in range(n):
    if map[i][j] == 1:
      house.append([i,j])
    elif map[i][j] == 2:
      chicken.append([i,j])

solve()
print(ans)