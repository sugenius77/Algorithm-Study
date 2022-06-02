import sys
n, k = map(int,sys.stdin.readline().split())

coin = []

for i in range(n):
  coin.append(int(sys.stdin.readline()))

coin.sort(reverse=True)

count = 0

for i in coin:
  if i <= k:
    count +=  k // i
    k = k % i

print(count)
   
