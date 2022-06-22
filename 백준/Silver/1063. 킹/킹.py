import sys
k, s, n = sys.stdin.readline().split()
direction = {
  'R':[0,1],'L':[0,-1],'B':[-1,0],'T':[1,0],
  'RT':[1,1],'LT':[1,-1],'RB':[-1,1],'LB':[-1,-1],
}
# 행, 열
king = [int(k[1]),ord(k[0])-65]
stone = [int(s[1]),ord(s[0])-65]
move = []

for i in range(int(n)):
  move.append(sys.stdin.readline().split())
  if 1 <= king[0] + direction[move[i][0]][0] <= 8 and 0 <= king[1] + direction[move[i][0]][1] < 8:
    king = [king[0] + direction[move[i][0]][0],king[1] + direction[move[i][0]][1]]
    if king == stone:
      if 1 <= stone[0] + direction[move[i][0]][0] <= 8 and 0 <= stone[1] + direction[move[i][0]][1] < 8:
        stone = [stone[0] + direction[move[i][0]][0], stone[1] + direction[move[i][0]][1]]
      else:
        king = [king[0] - direction[move[i][0]][0],king[1] - direction[move[i][0]][1]]
        
print(chr(65+king[1])+str(king[0]))
print(chr(65+stone[1])+str(stone[0]))