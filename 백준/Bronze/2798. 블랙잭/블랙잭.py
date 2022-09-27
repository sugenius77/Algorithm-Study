import sys

n,m = map(int,sys.stdin.readline().split())
array = list(map(int,sys.stdin.readline().split()))

def combinations(array,n):
  result = []
  if n == 0:
    return [[]]
  for i in range(len(array)):
    elem = array[i]
    for rest in combinations(array[i+1:],n-1):
      result.append([elem] + rest)
  return result

maximum = 0
for i in combinations(array,3):
  if sum(i) <= m and sum(i) > maximum:
    maximum = sum(i)

print(maximum)