import sys

bar = sys.stdin.readline()

stack = []
answer = 0

for i in range(len(bar)):
  if bar[i] == ')':
    # 레이저인 경우
    if bar[i-1] == '(':
      stack.pop()
      answer += len(stack)
    # 쇠막대기의 끝인 경우
    else:
      stack.pop()
      answer += 1
  else:
    stack.append(bar[i])

print(answer)