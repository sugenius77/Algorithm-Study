import sys

n = int(sys.stdin.readline())
time = [[] for _ in range(n)]

for i in range(n):
    time[i] = list(map(int, sys.stdin.readline().split()))

time.sort()
import heapq

room = []
heapq.heappush(room, time[0][1])

for i in range(1, n):
    if time[i][0] < room[0]:
        heapq.heappush(room, time[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, time[i][1])

print(len(room))
