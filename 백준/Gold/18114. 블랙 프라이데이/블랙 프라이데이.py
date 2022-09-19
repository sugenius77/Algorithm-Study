
import sys

def binarySearch(start,end,c,weight):
  while start <= end:
      mid = (start + end) // 2
      if weight[mid] == c:
          return mid
      if weight[mid] < c:
          start = mid + 1
      else:
          end = mid - 1
  return -1
  
def solve():
  if binarySearch(0, n - 1, c, weight) >= 0:# 고른 물건 1개
    return 1
  i = 0
  j = n - 1
  while i < j:
    sumW = weight[i] + weight[j]
    if sumW == c:
      return 1
    elif sumW > c:
      j -= 1
    else:
      diff = c - sumW
      if diff != weight[i] and diff != weight[j] and binarySearch(0, n - 1, diff, weight) >= 0:
        return 1
      i += 1
  return 0
  
n, c = map(int,sys.stdin.readline().split())
weight = list(map(int,sys.stdin.readline().split()))
weight.sort()      
print(solve())