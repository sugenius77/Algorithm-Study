# find 연산: 부모 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union 연산: 사이클이 발생하지 않는(부모 노드가 다른) 노드를 최소 신장 트리에 포함시키기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
def solution(n, costs):
    answer = 0
    edges = []
    
    # 부모 테이블 초기화
    parent = [0] * (n + 1)
    # 부모 테이블상에서, 부모를 자기 자신으로 초기화
    for i in range(1, n + 1):
        parent[i] = i
    
    for a,b,cost in costs:
        edges.append((cost,a,b))
    # 간선을 비용 순으로 정렬
    # edges = [(1, 0, 1), (1, 1, 3), (2, 0, 2), (5, 1, 2), (8, 2, 3)]
    edges.sort()
   
    # 간선을 하나씩 확인하며
    for edge in edges:
        cost, a, b = edge
        # 사이클이 발생하지 않는 경우에만(부모 노드가 다르면) 집합(최소 신장 트리)에 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost
            
    return answer
