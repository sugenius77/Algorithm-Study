import sys

n = int(sys.stdin.readline())
answer = 0
if n < 100:
  print(n)
else:
  for i in range(100,n+1):
    if eval(f'{str(i)[0]} - {str(i)[1]}') == eval(f'{str(i)[1]} - {str(i)[2]}'):
      answer += 1
  print(answer+99)