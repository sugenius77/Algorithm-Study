
def solution(n):
    answer = [0,1,2]
    if n < 3:
        return n
    for i in range(3,n):
        answer.append(answer[i-2] + answer[i-1]) 
    
    result = answer[-1] + answer[-2]
    return result % 1234567