import sys

# 듣도 못한 사람의 수, 보도 못한 사람의 수
n,m = map(int,sys.stdin.readline().split())

never_heard = set()
never_seen = set()

# 듣도 못한 사람들
for _ in range(n):
  never_heard.add(sys.stdin.readline().strip())
  
# 보도 못한 사람들
for _ in range(m):
  never_seen.add(sys.stdin.readline().strip())

# 듣도 보도 못한 사람들 = 두 집합의 교집합
result = never_heard.intersection(never_seen)

# 사전 순으로 정렬
result = sorted(result)

# 사람의 수 출력
print(len(result))
# 한 사람 씩 출력
for n in result:
  print(n)