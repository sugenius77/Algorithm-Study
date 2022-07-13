import sys

n, l = map(int,sys.stdin.readline().split())


while True:
  if ((2*n) - (l*(l-1))) % (2*l) == 0:
    answer = ((2*n) - (l*(l-1))) // (2*l)
    if answer < 0:
      print(-1)
      break
    else:
      print(*list(range(answer,answer+l)))
      break
  else:
    l += 1
  if l > 100:
    print(-1)
    break