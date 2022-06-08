import sys
from collections import deque

n = int(sys.stdin.readline())

deque = deque()

for i in range(n):
  order = sys.stdin.readline().rstrip()
  
  if order.startswith("push_front"):
    deque.appendleft(order[11:])
  if order.startswith("push_back"):
    deque.append(order[10:])
    
  if order == "pop_front":
    if deque:
      print(deque.popleft())
    else:
      print(-1)
      
  if order == "pop_back":
    if deque:
      print(deque.pop())
    else: 
      print(-1)
    
  if order == "size":
    print(len(deque))
    
  if order == "empty":
    if deque:
      print(0)
    else:
      print(1)
    
  if order == "front":
    if deque:
      print(deque[0])
    else:
      print(-1)
    
  if order == "back":
    if deque:
      print(deque[-1])
    else:
      print(-1)
