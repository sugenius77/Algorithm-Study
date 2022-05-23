import sys

n = int(sys.stdin.readline())
board = [[]for _ in range(n)]
for i in range(n):
  board[i]=list(map(int,sys.stdin.readline().split()))

dp = [0 for i in range(n+1)]

for i in range(n-1,-1,-1):
  if i + board[i][0] > n:
      dp[i] = dp[i+1]
  else:
      dp[i] = max(board[i][1] + dp[i + board[i][0]], dp[i+1])
  
print(dp[0])