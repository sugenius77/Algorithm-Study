import sys
import math
n = int(sys.stdin.readline())
students = list(map(int,sys.stdin.readline().split()))
b, c = map(int,sys.stdin.readline().split())
cnt = 0

for i in range(len(students)):
  cnt += 1
  students[i] = students[i] - b

for i in range(len(students)):
  if students[i] > 0:
    cnt += math.ceil(students[i]/c)
    
print(cnt)