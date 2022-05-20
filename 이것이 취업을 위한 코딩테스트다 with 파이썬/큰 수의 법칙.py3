
####### 첫번째 풀이 #######
import sys
### 1
# N, M, K 입력 받기
n, m, k = map(int,sys.stdin.readline().split())
# N개의 자연수
data = list(map(int, sys.stdin.readline().split()))
data.sort(reverse=True)
result = 0

### 2
while True:
  for i in range(k):
    if m == 0:
      break
    result += data[0]
    m -= 1
  if m == 0:
    break
  result += data[1]
  m -= 1

print(result)


####### 두번째 풀이 #######
import sys
### 1
# N, M, K 입력 받기
n, m, k = map(int,sys.stdin.readline().split())
# N개의 자연수
data = list(map(int, sys.stdin.readline().split()))
data.sort(reverse=True)

# 전체에서 가장 큰 수가 등장하는 횟수
count = (m // (k+1)) * k
# 반복되는 수열의 형태에서 가장 큰 수가 더해지는 횟수 

count += m % (k+1)
result = 0
result += count * data[0]
result += (m-count) * data[1]

print(result)
