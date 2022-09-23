def solution(s):
    zero = 0
    cnt = 0
    result = s
    while True:
        if result == '1':
            break
        result = ""    
        for i in s:
            if i == '1':
                result = result + i
            else:
                zero += 1
        s = bin(len(result))[2:]
        cnt += 1
    
    return [cnt,zero]