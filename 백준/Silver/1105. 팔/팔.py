import sys

l,r = sys.stdin.readline().split()
Llen = len(l)
Rlen = len(r)
cnt = 0


# 자리수가 다른 경우는 8이 없는 경우가 무조건 있기 때문에
if Llen != Rlen:
  print(0)
else:
  for i in range(Llen):
    if l[i] == r[i]:
      if l[i] == '8':
        cnt +=1
    else:
      break

  print(cnt)