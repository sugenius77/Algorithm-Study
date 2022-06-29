import sys
n = int(sys.stdin.readline())

current_num = 1
stack = []
# +,-를 삽입 할 배열
answer = []
# 수열 만드는게 불가능한지 아닌지 확인하는 Flag
flag = True

for _ in range(n):
  x = int(sys.stdin.readline())
  while current_num <= x:
    stack.append(current_num)
    current_num += 1
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
