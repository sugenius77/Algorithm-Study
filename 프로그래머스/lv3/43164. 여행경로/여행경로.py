from collections import defaultdict        
def solution(tickets):
    answer = []
    routes = defaultdict(list)
    # defaultdict(<class 'list'>, {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']})
    for key, value in tickets:
        routes[key].append(value)
    # defaultdict(<class 'list'>, {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['SFO', 'ICN']})
    for key in routes.keys():
        routes[key].sort(reverse=True)
        
    stack = ["ICN"]
    # stack이 비워질 때까지
    while stack:
        s = stack[-1]
        if not routes[s]:
            answer.append(stack.pop())
        else:
            stack.append(routes[s].pop())
    
    return answer[::-1]
