from collections import deque
def solution(maps):
    # 동,서,남,북
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    # 행 n, 열 m
    n = len(maps)
    m = len(maps[0])
    # 거리를 저장
    visited = [[0] * m for _ in range(n)]
    q = deque()
    # (0,0) 에서 시작
    q.append((0,0))
    visited[0][0] = 1
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
