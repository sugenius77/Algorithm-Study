def solution(want, number, discount):
    answer = 0
    cnt = 0
    for i in range(len(discount)):
        for j in range(len(want)):
            if discount[i:i+10].count(want[j]) == number[j]:
                cnt += 1
        if cnt == len(number):
            answer += 1
        cnt = 0
    return answer