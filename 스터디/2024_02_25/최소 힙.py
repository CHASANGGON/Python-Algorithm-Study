def enque(i):
    global last
    last += 1
    heap[last] = i
    c = last
    # 힙에 요소가 2개 이상일 때 정렬
    while heap[c//2] > heap[c]:
        heap[c//2], heap[c] = heap[c], heap[c//2]
        c //= 2

def deque():
    global last
    if last:
        r = heap[1]
        heap[1] = heap[last]
        heap[last] = 0
        last -= 1
        p = 1
        c = p*2
        # 최소힙을 유지
        while last >= c:
            if c+1 <= last and heap[c] > heap[c+1]:
                c += 1
            
            if heap[p] > heap[c]:
                heap[p], heap[c] = heap[c], heap[p]
                p = c
                c *= 2
            else:
                break

        return r

    # 아무것도 없으면 0을 반환
    else:
        return last

import sys
input = sys.stdin.readline

n = int(input())
heap = [0]*(n+1)
last = 0

for _ in range(n):
    i = int(input())
    
    if i:
        enque(i)
    else:
        print(deque())