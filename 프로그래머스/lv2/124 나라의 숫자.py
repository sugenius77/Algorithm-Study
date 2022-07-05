def solution(n):
    answer = ''
    country = ["4","1","2"]
    while n:
        answer = country[n % 3] + answer
        if n % 3 == 0:
            n = (n-1) //3
        else:
            n = n // 3

    return answer
