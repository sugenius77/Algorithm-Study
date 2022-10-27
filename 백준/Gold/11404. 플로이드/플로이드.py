import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

INF = int(1e9)
bus = [[INF] * n for _ in range(n)]

for i in range(m):
  a, b, c = map(int, sys.stdin.readline().split())
  if bus[a-1][b-1] > c:
    bus[a-1][b-1] = c
  
for i in range(n):
  for j in range(n):
    if i == j:
      bus[i][j] = 0

for k in range(n):
  for i in range(n):
    for j in range(n):
      if i != j:
        bus[i][j] = min(bus[i][j], bus[i][k] + bus[k][j])

for i in range(n):
  for j in range(n):
    if bus[i][j] == INF:
      print(0, end=" ")
    else:
      print(bus[i][j],end=" ")
  print()
