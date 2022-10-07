
def solution(cacheSize, cities):
    answer = 0
    cache = []
    for i in cities:
        i = i.lower()
        if cacheSize != 0:
            if i not in cache:
                if len(cache) == cacheSize:
                    cache.pop(0)    
                cache.append(i)
                answer += 5
            else:
                cache.pop(cache.index(i))
                cache.append(i)
                answer += 1
        else:
            answer += 5
            
    return answer