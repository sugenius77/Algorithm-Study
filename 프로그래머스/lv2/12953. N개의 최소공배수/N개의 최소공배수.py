import math
def solution(arr):
    answer = arr[0]
    for i in range(len(arr)):
        gcd = math.gcd(answer,arr[i])
        answer = (answer // gcd) * (arr[i] // gcd) * gcd

    return answer