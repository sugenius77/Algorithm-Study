def solution(str1, str2):
    answer = 0
    arr1 = []
    arr2 = []
    
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            arr1.append(str1[i:i+2].lower())
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            arr2.append(str2[i:i+2].lower())    
    
    intersection_list = set(arr1).intersection(set(arr2))
    union_list = set(arr1).union(set(arr2))
    
    if not arr1 and not arr2:
        return 65536
    inter, union = 0, 0
    for i in intersection_list:
        inter += min(arr1.count(i),arr2.count(i))
    
    for u in union_list:
        union += max(arr1.count(u),arr2.count(u))

    answer = int(inter / union * 65536)

    return answer 