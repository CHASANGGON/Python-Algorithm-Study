from collections import deque

# deque(데크, double-end queue)
# 양쪽에서 값을 삽입/삭제
# 데크 객체 생성 (초기화)
q = deque()
# 삽입 enqueue  (뒤에 원소를 추가)
q.append(1)  # 뒤에 원소를 추가
# q.appendleft(1) # 앞에 원소를 추가

# 삭제 dequeue (앞에서 원소를 삭제)
# q.pop() # 뒤에서 원소를 삭제
item = q.popleft()  # 앞에서 원소를 삭제
print(item)