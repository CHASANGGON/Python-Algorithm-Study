from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    cards = deque(list(map(int, input().split())))
    
    m, k = 0, 0
    cnt = 0
    
    while cnt < n:
        if cnt % 2: # 명우
            if cards[0] >= cards[-1]:
                m += cards.popleft()
            else:
                m += cards.pop()    
        
        else: # 근우
            if cards[0] >= cards[-1]:
                k += cards.popleft()
            else:
                k += cards.pop()
                
        cnt += 1

    print(k)
    
