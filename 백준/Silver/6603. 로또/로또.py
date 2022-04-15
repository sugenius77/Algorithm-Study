import sys
# 재귀함수를 이용한 조합 구현
def combination(arr, n):
  result = []
  if n == 0:
    return [[]]
  for i in range(len(arr)):
    elem = arr[i]
    for rest in combination(arr[i+1:],n-1):
      result.append([elem]+rest)
  return result

nums = [] 
while True:
  lst = list(map(int,sys.stdin.readline().split()))
  if lst[0] == 0:
    break
  for i in combination(lst[1:],6): 
    for j in i:
      print(j, end=" ")
    print()
  print()