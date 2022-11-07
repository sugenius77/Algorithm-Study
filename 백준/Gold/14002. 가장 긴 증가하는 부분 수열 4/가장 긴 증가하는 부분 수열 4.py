import sys

n = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
dp = [1] * n

for i in range(n):
  for j in range(i):
    if num[i] > num[j]:
      dp[i] = max(dp[i], dp[j]+1)

# 부분 수열의 길이
print(max(dp))

arr = []
m = max(dp)
for i in range(n-1,-1,-1):
  if dp[i] == m:
    arr.append(num[i])
    m -= 1

# 부분 수열
arr.reverse()
print(*arr)