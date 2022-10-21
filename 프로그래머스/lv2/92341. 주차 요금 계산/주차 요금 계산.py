import math
def toMinute(s):
    h,m = map(int,s.split(":"))
    return (h * 60) + m

def solution(fees, records):
    answer = []
    # 기본 시간, 기본 요금, 단위 시간, 단위 요금 순
    dt, df, ut, uf = fees
    dic = dict()
    for i in records:
        time, number, history = i.split()
        number = int(number)
        if number in dic:
            dic[number].append([toMinute(time), history])
        else:
            dic[number] = [[toMinute(time),history]]
            
    sortList = list(dic.items())
    sortList.sort(key=lambda x : x[0])
    
    for i in sortList:
        t = 0
        for j in i[1]:
            if j[1] == 'IN':
                t -= j[0]
            else:
                t += j[0]
        
        if i[-1][-1][1] == 'IN':
            t += toMinute("23:59")
        if t <= dt:
            answer.append(df)
        else:
            answer.append(df + (math.ceil((t - dt) / ut)) * uf)
                    
    return answer