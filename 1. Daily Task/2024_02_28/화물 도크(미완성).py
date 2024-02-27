from collections import deque
t = int(input())

for tc in range(1,t+1):
    n = int(input())
    
    cnt_lst = [0]*24
    a, b = map(int,input().split())
    for i in range(a,b):
        cnt_lst[i] += 1
    
    trucks = deque()
    for _ in range(n-1):
        trucks.append(list(map(int,input().split())))
        
    cnt = 1
    
    while True:
        a, b = trucks.popleft()
        if 1 in cnt_lst[a:b]:
            trucks.append([a,b])
        else:
            for i in range(a,b):
                cnt_lst[i] += 1
                