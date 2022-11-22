'''
사다리 게임은 n개의 세로선과 m개의 가로선
각각 세로선마다 가로선을 놓을 수 있는 위치의 개수 hasattr
'''

import sys

n,m,h = map(int,sys.stdin.readline().split())

# 2차원 배열로 사다리 만들기
ladder = [[0] * n for _ in range(h)]

for _ in range(m):
  a,b = map(int,sys.stdin.readline().split())
  ladder[a-1][b-1] = 1



# i번 세로선의 결과가 i번이 나오는지 확인하는 check 함수
def check():
  for i in range(n):
    tmp = i
    for j in range(h):
      if ladder[j][tmp] == 1:
        tmp += 1
      elif ladder[j][tmp-1] == 1:
        tmp -= 1
    if tmp != i:
      return False
  return True


def dfs(cnt, x, y):
    global ans
    if ans <= cnt:
        return
    if check():
        ans = min(ans, cnt)
        return
    if cnt == 3:
        return
    for i in range(x, h):
        k = y if i == x else 0
        for j in range(k, n - 1):
            if ladder[i][j]:
                j += 1
            else:
                ladder[i][j] = 1
                dfs(cnt + 1, i, j + 2)
                ladder[i][j] = 0

ans = 4
dfs(0, 0, 0)
print(ans if ans < 4 else -1)
