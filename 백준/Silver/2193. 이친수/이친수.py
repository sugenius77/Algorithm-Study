import sys

n = int(sys.stdin.readline())

dp = [0,1,1]

for i in range(3,91):
  dp.append(dp[i-2]+dp[i-1])

print(dp[n])