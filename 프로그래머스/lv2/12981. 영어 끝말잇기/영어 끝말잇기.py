def solution(n, words):
    answer = []
    stack = [words[0]]
    for i in range(len(words)-1):
        if words[i+1] in stack:
            answer = [(i+1) % n,(i+1)//n]
            break
        else:            
            stack.append(words[i+1])
        if not words[i].endswith(words[i+1][0]):
            answer = [(i+1) % n,(i+1)//n]
            break
    if stack == words:
        return [0,0]
    
    for i in range(2):
        answer[i] += 1
        
    return answer