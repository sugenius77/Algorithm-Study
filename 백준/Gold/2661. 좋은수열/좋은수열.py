import sys

n = int(sys.stdin.readline())
s = []

def back(depth):
  # 나쁜 수열인지 확인
  for i in range(1,(depth//2)+1):
    if s[-i:] == s[-2*i:-i]:
      return -1
      
  # n자리 수
  if depth == n:
    for i in range(n):
      print(s[i],end = '')
    return 0
      
  for i in range(1,4):
    s.append(i)
    if back(depth+1) == 0:
      return 0
    s.pop()

back(0)
