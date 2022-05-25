import sys

# 현재 나이트의 위치
now = sys.stdin.readline()
x = int(now[1])
y = int(ord(now[0])) - int(ord('a')) + 1
cnt = 0

# 나이트가 이동할 수 있는 8가지의 뱡항 정의
steps = [(-2,-1),(-2,1),(-1,2),(-1,-2),(1,-2),(1,2),(2,-1),(2,1)]


for i in range(len(steps)):
  nx = x + steps[i][1] 
  ny = y + steps[i][0]
  if 1 > nx or nx > 8 or ny < 1 or  ny > 8:
    continue
  cnt += 1

print(cnt)
