import sys

n = int(sys.stdin.readline())

# n개의 원판을 start에서 end로 옮기기
def hanoi(n, start, end):
    if n == 1 :
        print(start, end)
        return
    # 1단계
    hanoi(n-1, start, 6-start-end) 
    # 2단계
    print(start, end) 
    # 3단계
    hanoi(n-1, 6-start-end, end)
    

print(2**n-1)
hanoi(n, 1, 3)