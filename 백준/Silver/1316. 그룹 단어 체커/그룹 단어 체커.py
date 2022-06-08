import sys

n = int(sys.stdin.readline())
cnt = 0


for _ in range(n):
  word = list(sys.stdin.readline().strip())
  tmp = []
  for i in range(len(word)):
    # 중복이 없을 경우
    if len(word) == len(set(word)):
      cnt += 1
      break
    # 중복이 있을 경우
    elif word[i] not in tmp or tmp[-1] == word[i]:
        tmp.append(word[i])
    if len(word) == len(tmp):
      cnt += 1
      
print(cnt)