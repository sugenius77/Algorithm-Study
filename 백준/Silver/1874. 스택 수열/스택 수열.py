import sys
n = int(sys.stdin.readline())

i = 1
stack = []
answer = []
flag = True
for _ in range(n):
  x = int(sys.stdin.readline())
  while i <= x:
    stack.append(i)
    i += 1
    answer.append('+')
  if stack[-1] == x:
    stack.pop()
    answer.append('-')
  else:
    flag = False


if not flag:
  print('NO')
else:
  for s in answer:
    print(s)