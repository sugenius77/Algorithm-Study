from collections import deque
def solution(maps):
    visited = [[0] * (len(maps[0])) for _ in range(len(maps))]
    return bfs(0,0,maps,visited)
def bfs(x,y,maps,visited):
    # 동,서,남,북
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    # 행 n, 열 m
    n = len(maps)
    m = len(maps[0])        
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1
                maps[nx][ny] = 0
                

    return visited[-1][-1] if visited[-1][-1] else -1
