import sys

N = int(sys.stdin.readline())

cnt = 0
for i in range(N+1):
  for j in range(60):
    for z in range(60):
      if '3' in str(i)+str(j)+str(z):
        print(i,j,z)
        cnt += 1

print(cnt)
        
