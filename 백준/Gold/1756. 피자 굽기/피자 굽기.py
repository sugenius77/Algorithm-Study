import sys
d, n = map(int,sys.stdin.readline().split())

oven = list(map(int,sys.stdin.readline().split()))
dough = list(map(int,sys.stdin.readline().split()))

# 오븐의 길이에 따라 들어갈 수 있는 반죽의 크기
# [5, 5, 4, 3, 3, 2, 2]
for i in range(1,d):
  if oven[i] > oven[i-1]:
    oven[i] = oven[i-1]

flag = 0
for i in range(d-1, -1, -1):
  if dough[flag] <= oven[i]:    
    flag += 1

  if flag == n:
    print(i+1)
    break

if flag != n:
  print(0)