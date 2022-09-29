def solution(n):
    answer = []
    for i in range(n+1):
        if i == 0:
            print(i)
            answer.append(0)
        elif i == 1 or i == 2:
            answer.append(1)
        else:
            answer.append(answer[i-2]+answer[i-1])
    return answer[-1] % 1234567