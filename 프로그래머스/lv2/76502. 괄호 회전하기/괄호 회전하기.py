def solution(s):
    answer = 0
    array = list(s)
    for j in range(len(s)):
        array = s[j:] + s[:j]
        if array[0] in (']',')','}'):
            continue
        else:
            stack = [array[0]]
            for i in range(1,len(array)):
                if len(stack) == 0 and array[i] in (']',')','}'):
                    continue
                else:
                    if array[i] in ('[','(','{'):
                        stack.append(array[i])
                    elif stack[-1] == '[' and array[i] == ']':
                        stack.pop(-1)
                    elif stack[-1] == '(' and array[i] == ')':
                        stack.pop(-1)
                    elif stack[-1] == '{' and array[i] == '}':            
                        stack.pop(-1)
                        
            if len(stack) == 0:
                answer += 1

    return answer

