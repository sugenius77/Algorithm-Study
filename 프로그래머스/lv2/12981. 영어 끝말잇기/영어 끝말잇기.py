def solution(n, words):
    answer = []
    stack = [words[0]]
    for i in range(1,len(words)):
        if words[i] in stack:
            answer = [(i % n) + 1,(i//n) +1]
            break
        else:            
            stack.append(words[i])
        if not words[i-1].endswith(words[i][0]):
            answer = [(i % n) + 1 ,(i//n) +1]
            break
    if stack == words:
        return [0,0]
    return answer