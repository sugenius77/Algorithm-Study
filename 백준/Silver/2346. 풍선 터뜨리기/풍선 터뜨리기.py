import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
result = []
index = [i for i in range(1,n+1)]
idx = 0
now = array.pop(idx)
result.append(index.pop(idx))

while array:
  if now < 0:
    idx = (now + idx) % len(array)
    
  else:
    idx = (now + idx -1) % len(array)
  now = array.pop(idx)
  result.append(index.pop(idx))

print(*result)
