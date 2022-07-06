import sys

n = int(sys.stdin.readline())
people = list(map(int,sys.stdin.readline().split()))

height = [0] * n

for i in range(n):
  cnt = 0
  for j in range(n):
    if cnt == people[i] and height[j] == 0:
      height[j] = i + 1
      break
    elif height[j] == 0:
      cnt += 1
    
print(*height)
