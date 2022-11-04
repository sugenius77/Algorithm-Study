def solution(dirs):
    x,y = 0,0
    visited = set()
    direction = {'U':[0,1],'D':[0,-1],'R':[1,0],'L':[-1,0]}
    
    for i in dirs:
        if -5 <= x + direction[i][0] <= 5 and -5 <= y + direction[i][1] <= 5:
            visited.add(((x,y),(x + direction[i][0], y + direction[i][1])))
            visited.add(((x + direction[i][0], y + direction[i][1]), (x,y)))
            x,y = x + direction[i][0], y + direction[i][1]
    
    return len(visited)//2