def convert(num, base):
    temp = "0123456789ABCDEF"
    # 몫, 나머지
    q, r = divmod(num,base)
    if q == 0:
        return temp[r]
    else:
        return convert(q,base) + temp[r]
    
def solution(n, t, m, p):
    answer = ''
    test = ''
    for i in range(m*t):
        test += str(convert(i,n))
    while len(answer) < t:
        answer += test[p-1]
        p += m
    return answer