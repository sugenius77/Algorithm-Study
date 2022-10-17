
import sys

n,k = map(int,sys.stdin.readline().split())

dp = [0] * 100001

knapsack = [[0] * (k+1) for _ in range(n+1)]

stuff = [[0,0]]

for _ in range(n):
  stuff.append(list(map(int,sys.stdin.readline().split())))


for i in range(1, n+1):
  for j in range(1, k+1):
    w = stuff[i][0]
    v = stuff[i][1]

    if j < w:
      knapsack[i][j] = knapsack[i-1][j]
    else:
      knapsack[i][j] = max(v + knapsack[i-1][j-w],knapsack[i-1][j])

print(knapsack[n][k])