def solution(s):
    # 제거할 0의 개수
    zero = 0
    # 이진 변환한 횟수
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