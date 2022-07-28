import sys

# 가장 긴 연속되는 부분 찾는 함수
def check(arr):
    n = len(arr)
    answer = 1
    # 열을 순회하면서 연속되는 숫자 세기
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            # 비교해서 현재 cnt가 더 크다면 answer 갱신하기
            if cnt > answer:
                answer = cnt
        cnt = 1
        # 행을 순회하면서 연속되는 숫자 세기
        for j in range(1, n):
            if arr[j][i] == arr[j - 1][i]:
                cnt += 1
            else:
                cnt = 1
            # 비교해서 현재 cnt가 더 크다면 answer 갱신하기
            if cnt > answer:
                answer = cnt
    return answer


n = int(sys.stdin.readline())
arr = [list(sys.stdin.readline()) for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(n):
        # n보다 작으면 열을 바꿀 수 있다
        if j + 1 < n:
            # 인접한 것과 바꾸기
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            temp = check(arr)
            if temp > answer:
                answer = temp
            # 바꿨던 것을 다시 원래대로 돌려놓기
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]

        #  n보다 작으면 행을 바꿀 수 있다
        if i + 1 < n:
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
            temp = check(arr)
            if temp > answer:
                answer = temp
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]

print(answer)