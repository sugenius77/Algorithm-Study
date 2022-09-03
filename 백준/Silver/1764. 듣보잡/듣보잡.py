import sys

# 듣도 못한 사람의 수, 보도 못한 사람의 수
n,m = map(int,sys.stdin.readline().split())

never_heard = set()
never_seen = set()

# 듣도 못한 사람들
for _ in range(n):
  never_heard.add(sys.stdin.readline().strip())
# 보도 못한 사람의 수
for _ in range(m):
  never_seen.add(sys.stdin.readline().strip())

result = never_heard.intersection(never_seen)
result = sorted(result)
print(len(result))
for n in result:
  print(n)