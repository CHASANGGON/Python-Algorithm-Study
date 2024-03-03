from collections import deque

q = deque()

q.append(1)
q.append(1)

q.append(1)

nq = q

print(nq)

nq.clear()

print(nq)