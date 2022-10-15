import sys

n = int(sys.stdin.readline())
card = list(map(int,sys.stdin.readline().split()))
card.sort()

m = int(sys.stdin.readline())
check = list(map(int,sys.stdin.readline().split()))

def binary_search(arr,target,start,end):
  while start <= end:
    mid = (start + end) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] > target:
      end = mid - 1
    else: 
      start = mid + 1
  return None

for i in range(m):
  if binary_search(card, check[i], 0, n-1) is not None:
    print(1,end=' ')
  else:
    print(0,end=' ')