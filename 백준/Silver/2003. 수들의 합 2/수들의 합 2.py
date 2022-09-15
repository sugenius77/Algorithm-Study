import sys

n, m = map(int,sys.stdin.readline().split())
array = list(map(int,sys.stdin.readline().split()))

cnt = 0

left = 0
right = left + 1

while right <= n and left <= right:
  total = sum(array[left:right])
  if total == m:
    cnt += 1
    left += 1
    right = left + 1
  if total < m:
    right += 1
  if total > m:
    left += 1
    right = left + 1

print(cnt)