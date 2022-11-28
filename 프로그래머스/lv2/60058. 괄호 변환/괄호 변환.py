# 올바른 괄호 문자열인지 확인하는 함수
def check(c):
    stack = []
    for i in c:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True
# 문자열 p를 u, v로 분리하는 함수
def divide(p):
    open_p = 0
    close_p = 0
    for i in range(len(p)):
        if p[i] == '(':
            open_p += 1
        else:
            close_p += 1
        if open_p == close_p:
            return p[:i+1], p[i+1:]
            
def solution(p):
    # 1
    if not p:
        return ''
    
    # 2
    u,v = divide(p)
    
    # 3
    if check(u):
        return u + solution(v)
    # 4
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        
        for i in u[1:len(u)-1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
        return answer