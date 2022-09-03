import sys
from collections import deque

n = int(sys.stdin.readline())

# 기술 번호
tech = list(map(int,sys.stdin.readline().split()))
# 바닥에 내려놓은 카드 (1,2,3,4,5)
card = deque(range(1,n+1))
# 초기 카드의 상태
origin = deque()

while card:
  t = tech.pop()
  c = card.popleft()
  if t == 1:
    origin.appendleft(c)
  if t == 2:
    origin.insert(1,c)
  if t == 3:
    origin.append(c)

print(*origin)