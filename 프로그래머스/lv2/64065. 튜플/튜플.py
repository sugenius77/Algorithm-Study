from collections import defaultdict
def solution(s):
    answer = []
    dict = defaultdict(int)
    tmp = []
    # 문자열 파싱
    new_s = s.split('}')[:-2]
    for i in new_s:
        tmp.append(i[2:].split(','))
    
    # 갯수 세기
    for i in tmp:
        for j in i:
            dict[j] += 1
    
    # 딕셔너리 value 값을 기준으로 정렬
    result = sorted(dict.items(),key = lambda x :x[1],reverse = True)
    
    # 키 값만 리스트에 넣기
    for i in result:
        answer.append(int(i[0]))
        
    return answer