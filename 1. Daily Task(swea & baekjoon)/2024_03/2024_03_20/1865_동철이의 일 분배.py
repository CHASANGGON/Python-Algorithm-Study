def backtrack(i, multiple):
    global max_multiple
    
    if multiple <= max_multiple:
        return
    
    if i == n:
        max_multiple = multiple
        return
    
    for j in range(i, n):
        p[i], p[j] = p[j], p[i]
        backtrack(i+1, multiple*(arr[i][p[i]]/100))
        p[i], p[j] = p[j], p[i]

t = int(input())

for tc in range(1,t+1):
    
    n = int(input())
    
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    p = list(range(n))
    max_multiple = 0
    backtrack(0,1)
    
    print(f'#{tc} {max_multiple*100:.6f}')