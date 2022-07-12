def solution(a, b):
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    end_date = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    # 3의 1일의 요일
    n = sum(end_date[:a-1]) + b
    
    aa = n % 7
    answer = day[aa-1]
    # 3월 24일 요일
    # tmp  = 7  * (b // 7) + 1
    
#     print(n,tmp)
#     answer = day[day.index(day[n]) + (b - tmp)]
    # answer = 0
    return answer

# print(solution(3,31))