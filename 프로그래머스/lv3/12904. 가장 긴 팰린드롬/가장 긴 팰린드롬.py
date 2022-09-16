def solution(s):
    answer = 0
    for i in range(len(s)):
        for j in range(len(s),i,-1):
            if s[i:j+1] == s[i:j+1][::-1]:
                answer = max(answer,len(s[i:j+1]))
            
                # print(s[i:j+1])
    return answer