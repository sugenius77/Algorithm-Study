import sys

n,m = map(int,sys.stdin.readline().split())

name_book = []
book = {}

for i in range(n):
  pk = sys.stdin.readline().rstrip()
  name_book.append(pk)
  book[pk] = i+1

for _ in range(m):
  problem = sys.stdin.readline().rstrip()
  if problem.isdigit():
    print(name_book[int(problem)-1])
  else:
    print(book[problem])