
def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse = True)
    for i in range(len(A)):
        multiply = A[i] * B[i]
        answer += multiply
    return answer