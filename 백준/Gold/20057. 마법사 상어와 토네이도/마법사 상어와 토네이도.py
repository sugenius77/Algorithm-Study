import sys 

# 입력 받기
n = int(sys.stdin.readline())
desert = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

# 토네이도 시작점
now = [n//2,n//2]

# 위치와 비율
left = [(-2, 0, 0.02), (2, 0, 0.02), (-1, -1, 0.1), (-1, 0, 0.07), (-1, 1, 0.01), (1, -1, 0.1), (1, 0, 0.07), (1, 1, 0.01), (0, -2, 0.05), (0, -1, 0)]  
right = [(x,-y,rate) for x, y,rate in left]
down = [(-y,x,rate) for x, y,rate in left]
up = [(-x,y,rate) for x, y,rate in down]


answer = 0

def move(cnt,dx,dy,direction):
  global answer
  for _ in range(cnt+1):
    now[0], now[1] = now[0] + dx, now[1] + dy
    # 범위 밖이면 break
    if now[0] < 0 or now[1] < 0: 
      break 
    # 퍼진 모래를 누적한 양  
    spreads = 0 
    for dx, dy, r in direction:
      nx,ny = now[0] + dx, now[1] + dy
      # 퍼지지 않는 모래들은 현재 자리에 누적해주기 (알파)
      if r == 0: 
        sand = desert[now[0]][now[1]] - spreads 
      # 퍼지는 모래들 계산 
      else:
        sand = int(desert[now[0]][now[1]] * r)
      # 범위 안   
      if 0 <= nx < n and 0 <= ny < n:
        desert[nx][ny] += sand 
      # 범위 밖: 정답 누적 값 업데이트    
      else: 
        answer += sand 
      # 현재 자리 계산을 위한 퍼지는 모래의 누적값   
      spreads += sand  

for i in range(n):  
  if i % 2 == 0: 
    move(i, 0, -1, left) # 왼쪽 
    move(i, 1, 0, down)  # 아래쪽 
  else:
    move(i, 0, 1, right) # 오른쪽 
    move(i, -1, 0, up)  # 위쪽 

print(answer)