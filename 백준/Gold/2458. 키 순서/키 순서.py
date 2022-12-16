import sys
n, m = map(int,sys.stdin.readline().split())
height = [[0] * (n+1) for _ in range(n+1)]
        
for _ in range(m):
  short, tall = map(int,sys.stdin.readline().split())
  height[tall][short] = 1

# 플로이드 와샬
for k in range(1,n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      if height[i][k] == 1 and height[k][j] == 1:
        height[i][j] = 1


answer = 0
for i in range(1,n+1):
  check = 0
  for j in range(1,n+1):
    check += (height[i][j] + height[j][i])
  if check == (n-1):
    answer += 1

print(answer)