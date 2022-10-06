'''
1. 1번 정점부터 n번 정점으로 최단 거리로 이동
2. 임의로 주어진 두 정점은 반드시 통과
3. 한번 이동했던 정점, 간선 다시 이동 가능
'''

import sys

# 정점 n ,간선 e
n,e = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
# 무방향 그래프
# a정점에서 b정점까지 거리(가중치)는 c
for i in range(e):
  a,b,c = map(int,sys.stdin.readline().split())
  graph[a].append((b,c))
  graph[b].append((a,c))


# 반드시 거쳐야하는 서로 다른 두 개의 정점
v1,v2 = map(int,sys.stdin.readline().split())

INF = 1e9


import heapq
def dijkstra(start):
  distance = [INF] * (n+1)
  q = []
  heapq.heappush(q,(0,start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))
  # start부터 n까지 가는 최단 거리
  return distance

# 출발점 1,v,vv에서 n까지의 최단 거리
original_dist = dijkstra(1)
v1_dist = dijkstra(v1)
v2_dist = dijkstra(v2)


# 두가지 방법
# 시작점 -> v -> vv -> n
# 시작점 -> vv -> v -> n
v1_v2 = original_dist[v1] + v1_dist[v2] + v2_dist[n]
v2_v1 = original_dist[v2] + v2_dist[v1] + v1_dist[n]

ans = min(v1_v2,v2_v1)

print(ans if ans < INF else -1)

