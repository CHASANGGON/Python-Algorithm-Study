def backtrack(i, s):
    global min_s
    if s >= min_s:
        return
    
    if i == n:
        min_s = min(min_s,s)
        return
        
    for j in range(i,n):
        p[i], p[j] = p[j], p[i]
        backtrack(i+1, s+arr[i][p[i]])
        p[i], p[j] = p[j], p[i]
        

t = int(input())

for tc in range(1,t+1):
    
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    
    p = list(range(n))
    min_s = 999999999
    
    backtrack(0,0)
    
    print(f'#{tc} {min_s}')