def solution(skill, skill_trees):
    answer = 0
    
    for i in skill_trees: 
        # ['C','B','D']
        skill_list = list(skill)
        for j in i:
            if j in skill:
                if j != skill_list.pop(0):
                    break

                    
        else:
            answer += 1
                    
    return answer   