### 나의 풀이
```python
import sys

n, m = map(int,sys.stdin.readline().split())
data = []
for i in range(n):
  data.append(list(map(int,sys.stdin.readline().split())))
  
min_list = []
for i in data:
  min_list.append(min(i))

print(max(min_list))

```
### 다른 풀이1 (min()함수 사용)
```python 
import sys
n, m = map(int,sys.stdin.readline().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
  data = list(map(int,sys.stdin.readline().split()))
  # 현재 줄에서 가장 작은 수 찾기
  min_value = min(data)
  # 가장 작은 수들 중에서 가장 큰 수 찾기
  result = max(result,min_value)
  
print(result)
```
### 다른 풀이2 (2중 반목문 사용)
```python
import sys

n, m = map(int,sys.stdin.readline().split())

result = 0
for i in range(n):
  data = list(map(int,sys.stdin.readline().split()))
  # 현재 줄에서 가장 작은 수 찾기
  # min_value의 초기값을 10001 (카드에 적힌 숫자들의 법위는 1 이상 10000이하)
  min_value = 10001
  for a in data:
    min_value = min(min_value,a)
  # 가장 작은 수들 중에서 가장 큰 수 찾기
  result = max(result,min_value)

print(result)
```
