# 루트에 가장 큰 수를 유지하면 됨
# 그러므로 어떤 수가 들어오면
# 일단 완전 트리에 맞게 추가하고
# 그 후 크기에 맞게 순서를 조정한다
def enque(a):
    global last
    last += 1
    heap[last] = a
    c = last
    while c > 1 and heap[c//2] < heap[c]:
        heap[c//2], heap[c] = heap[c], heap[c//2]
        c //= 2

def deque():
    global last
    if last:
        r = heap[1]
        heap[1] = heap[last]
        last -= 1
        p = 1
        c = 1*2
        while last >= c:
            if heap[c] < heap[c+1]:
                c += 1
            if heap[p] < heap[c]:
                heap[p], heap[c] = heap[c], heap[p]
                p = c
                c = p*2
            else:
                break
        return r
    else:
        return last

import sys
input = sys.stdin.readline

n = int(input())

last = 0
heap = [0]*(n+1)

for _ in range(n):
    a = int(input())
    if a:
        enque(a)
    else:
        print(deque())