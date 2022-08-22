import sys

n, m = map(int, sys.stdin.readline().split())
board = []
count =[]
for _ in range(n):
    board.append(sys.stdin.readline().strip())

# 전체 체스판에서의 시작점 x,y
for x in range(n-7):
  for y in range(m-7):
    # W로 시작할 경우 바뀐 정사각형의 갯수
    cnt_w = 0
    # B로 시작할 경우 바뀐 정사각형의 갯수
    cnt_b = 0
    # a,b를 시작점으로 8칸씩 체크
    for i in range(x,x+8):
      for j in range(y,y+8):
        # i와 j의 합이 짝수 -> 시작점과 같은 색깔
        if (i+j) % 2 == 0:
          if board[i][j] != "W":
            cnt_w += 1
          if board[i][j] != "B":
            cnt_b += 1
        # i와 j의 합이 홀수 -> 시작점과 다른 색깔
        else:
          if board[i][j] != "B":
            cnt_w += 1
          if board[i][j] != "W":
            cnt_b += 1
    count.append(min(cnt_w, cnt_b))
print(min(count))
    
  