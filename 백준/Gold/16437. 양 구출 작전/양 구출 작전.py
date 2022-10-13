import sys
sys.setrecursionlimit(1000000)
n = int(sys.stdin.readline())

node = [[],[0,0]]
tree = [[] for _ in range(n+2)]

for i in range(1,n):
  t, a, p = sys.stdin.readline().split()
  a = int(a)
  p = int(p)
  node.append([t,a,p])
  tree[p].append(i+1)
  
def dfs(v):
  result = 0
  
  # 노드를 탐색해서 더해준다.
  for i in tree[v]:
    result += dfs(i)

  # 노드의 타입이 늑대라면 빼준다
  if node[v][0] == 'W':
    result -= node[v][1]
    if result < 0:
      result = 0
  
  # 노드의 타입이 양이라면 더해준다
  else:
    result += node[v][1]
  return result

print(dfs(1))
  