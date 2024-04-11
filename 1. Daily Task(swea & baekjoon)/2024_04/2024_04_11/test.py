import heapq

# 간선 리스트
edges = []

# 간선 추가
heapq.heappush(edges, [1, 2, 6])
heapq.heappush(edges, [2, 3, 4])
heapq.heappush(edges, [3, 1, 1])
heapq.heappush(edges, [1, 2, 5])
heapq.heappush(edges, [1, 2, 4])
heapq.heappush(edges, [1, 3, 1])

# 결과 출력
print(edges)