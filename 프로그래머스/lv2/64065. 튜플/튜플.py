from collections import defaultdict
def solution(s):
    answer = []
    dict = defaultdict(int)
    new_s = s.split('}')[:-2]
    for i in new_s:
        answer.append(i[2:].split(','))

    for i in answer:
        for j in i:
            dict[j] += 1
            
    result = sorted(dict.items(),key = lambda x :x[1],reverse = True)
    res = []
    for i in result:
        res.append(int(i[0]))
        
    return res