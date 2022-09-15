import sys
s, c = map(int,sys.stdin.readline().split())
scallion = [int(sys.stdin.readline()) for _ in range(s)]

scallion.sort()

# 파닭에 들어가는 파의 개수
def slice(len, scallion):
  cnt = 0
  for i in scallion:
    cnt += i // len
  return cnt
  
start = 1
end = max(scallion)
# 파닭에 들어가는 최대 파의 길이
maxS = 0

while end >= start:
  mid = (end + start) // 2
  # 파닭에 들어가는 파의 개수가 파닭의 수보다 크거나 같다면
  if slice(mid, scallion) >= c:
    maxS = mid
    start = mid + 1
  # 파닭에 들어가는 파의 개수가 파닭의 수보다 작다면
  else:
    end = mid - 1

# 라면에 들어가는 파의 양 = 전체 파의 양 - 사용한 파의 양
answer = sum(scallion) - maxS * c
print(answer)