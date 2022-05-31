import sys
n = int(sys.stdin.readline())

switch = list(map(int,sys.stdin.readline().split()))

student = int(sys.stdin.readline())

# for문 range범위 잘 설정하기
for _ in range(student):
  s, num = map(int,sys.stdin.readline().split())
  # 남학생일 때
  if s == 1:
    for i in range(1,n//num+1):
      if switch[i*num-1] == 1:
        switch[i*num-1] = 0
      else:
        switch[i*num-1] = 1
  # 여학생일 때
  if s == 2:
    if switch[num-1] == 1:
      switch[num-1] = 0
    else:
      switch[num-1] = 1      
    for j in range(1,n//2+1):
      if num-1-j >= 0 and num-1+j < n:
        if switch[num-1+j] == switch[num-1-j]:
          if switch[num-1+j] == 0:
            switch[num-1+j] = 1
            switch[num-1-j] = 1
          else:
            switch[num-1+j] = 0
            switch[num-1-j] = 0
        else:
          break

for i in range(len(switch)):
  if i != 0 and i % 20 == 0:
    print("")
    print(switch[i], end=" ")
  else:
    print(switch[i], end=" ")
