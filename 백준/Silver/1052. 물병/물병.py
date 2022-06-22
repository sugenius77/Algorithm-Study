import sys
n, k = map(int,sys.stdin.readline().split())

bottle = 0
while bin(n).count('1') > k:
  x = 2 ** (bin(n)[::-1].index('1'))
  bottle += x
  n += x

print(bottle)

  
  