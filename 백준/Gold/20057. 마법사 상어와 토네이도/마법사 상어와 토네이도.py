import sys 

n = int(sys.stdin.readline())
desert = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]


# 토네이도 시작점
now = [n//2,n//2]

# 위치와 비율
left = [(-2, 0, 0.02), (2, 0, 0.02), (-1, -1, 0.1), (-1, 0, 0.07), (-1, 1, 0.01), (1, -1, 0.1), (1, 0, 0.07), (1, 1, 0.01), (0, -2, 0.05), (0, -1, 0)] 
right = [(x,-y,rate) for x, y,rate in left]
down = [(-y,x,rate) for x, y,rate in left]
up = [(-x,y,rate) for x, y,rate in down]

 
rate = {'left': left, 'right': right, 'down': down, 'up': up} 

answer = 0

def move(cnt,dx,dy,direction):
  global answer
  for _ in range(cnt+1):
    now[0],now[1] = now[0]+ dx, now[1] + dy
    
    if now[0] < 0 or now[1] < 0: 
      break 
    spreads = 0 #모래가 퍼진값을 누적한 양  
    for dx,dy,r in rate[direction]:
      nx,ny = now[0] + dx, now[1] + dy
      if r == 0: #퍼지지 않는 모래들은 현재 자리에 누적해주기
        sand = desert[now[0]][now[1]] - spreads 
      else:#퍼지는 모래들 계산 
        sand = int(desert[now[0]][now[1]] * r)
      if 0 <= nx < n and 0 <= ny < n:#범위안 
        desert[nx][ny] += sand 
      else: #범위밖: 정답 누적값 업데이트  
        answer += sand 
      spreads += sand  #현재자리 계산을 
      
for i in range(n): 
  if i % 2 == 0: 
    move(i, 0, -1, 'left') #왼쪽 
    move(i, 1, 0, 'down')  #아래쪽 
  else: 
    move(i, 0, 1, 'right') #오른쪽 
    move(i, -1, 0, 'up')  #위쪽 

print(answer)