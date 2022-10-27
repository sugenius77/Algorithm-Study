import sys

strA = sys.stdin.readline().strip()
strB = sys.stdin.readline().strip()

n = len(strA)
m = len(strB)

LCS = [[0] * (m+1) for _ in range(n+1)]

for i in range(1,n+1): 
  for j in range(1,m+1):
    if strA[i-1] == strB[j-1]:
      LCS[i][j] = LCS[i-1][j-1] + 1
    else:
      LCS[i][j] = max(LCS[i-1][j],LCS[i][j-1])


result = []

i = n 
j = m 
while i > 0 and j > 0:
  if LCS[i][j] == LCS[i-1][j]:
    i -= 1
  elif LCS[i][j] == LCS[i][j-1]:
    j -= 1
  else:
    result.append(strA[i-1])
    i -= 1
    j -= 1

print(LCS[-1][-1])
for i in result[::-1]:
  print(i,end="")
