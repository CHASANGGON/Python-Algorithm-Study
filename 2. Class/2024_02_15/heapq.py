import heapq

# 기본적으로 리스트 자료형을 사용하여 동작 수행...
hq = []  # 힙으로 사용할 리스트

# 우선순위큐에 값을 삽입하는 연산 enqueue -> heappush 함수
heapq.heappush(hq, 30)
heapq.heappush(hq, 10)
heapq.heappush(hq, 50)
heapq.heappush(hq, 100)
heapq.heappush(hq, 0)

# 우선순위큐에 삭제를 하는 연산 dequeue -> heappop 함수
item = heapq.heappop(hq)
print(item)

item = heapq.heappop(hq)
print(item)

item = heapq.heappop(hq)
print(item)

item = heapq.heappop(hq)
print(item)

item = heapq.heappop(hq)
print(item)