def solution(elements):
    answer = 0
    result = set()
    n = 0
    while n != len(elements):
        n += 1
        for i in range(len(elements)):
            if i+n > len(elements):
                # if sum(elements[i:]+elements[:i+n-len(elements)]) not in result:
                result.add(sum(elements[i:]+elements[:i+n-len(elements)]))
            else:
                # if sum(elements[i:i+n]) not in result:
                result.add(sum(elements[i:i+n]))
        

    return len(result)