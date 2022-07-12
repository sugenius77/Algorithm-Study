def solution(a, b):
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    end_date = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    # 입력 날짜까지의 일수 계산
    n = sum(end_date[:a-1]) + b
    
    # 요일 구하기
    idx = n % 7

    return day[idx-1]
