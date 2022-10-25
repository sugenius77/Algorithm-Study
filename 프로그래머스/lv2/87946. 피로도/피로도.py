from itertools import permutations
def solution(k, dungeons):
    idx = [i for i in range(len(dungeons))]
    cnt = len(dungeons)
    
    for i in range(cnt,0,-1):
        for order in permutations(idx,i):
            now = k
            check = True
            for o in order:
                if dungeons[o][0] > now:
                    check = False
                    break
                else: 
                    now -= dungeons[o][1]
            if check:
                return i
          