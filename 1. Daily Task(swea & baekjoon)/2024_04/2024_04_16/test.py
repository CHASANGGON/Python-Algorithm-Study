from collections import deque

lst = [[1,1],[1,1],[2,2],[2,2],[3,3]]
lst = deque(set(lst))
print(lst)
print(lst.popleft())