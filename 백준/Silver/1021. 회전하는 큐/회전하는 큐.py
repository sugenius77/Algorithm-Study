from collections import deque
import sys

n,m = map(int, sys.stdin.readline().split())

array = list(map(int,sys.stdin.readline().split()))

q = deque([])
[q.append(i) for i in range(1,n+1)]


cnt = 0
i = 0

while i != m:
  if q[0] == array[i]:
    q.popleft()
    i += 1
  else:
    Rlen = len(q) - q.index(array[i])
    Llen = q.index(array[i])
    if Rlen > Llen:
      q.rotate(-Llen)
      cnt += Llen
      q = q
    else:
      q.rotate(Rlen)
      cnt += Rlen
      q = q

print(cnt)
      
    
    