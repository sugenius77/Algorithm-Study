import sys
n = int(sys.stdin.readline())

array = []

def sum_num(str):
  result = 0
  for i in str:
    if i.isdigit():
      result += int(i)
  return result
  
for _ in range(n):
  array.append(sys.stdin.readline().strip())

array.sort(key = lambda x:(len(x),sum_num(x),x))

for i in array:
  print(i)