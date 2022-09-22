def solution(s):    
    answer = ""
    chk = 1
    for i in range(len(s)):
        if s[i] == " ":
            answer += " "
            chk = 1
        else:
            if chk == 1:
                answer += s[i].upper()
                chk = 0
            elif chk == 0:
                answer += s[i].lower()
        

    return answer