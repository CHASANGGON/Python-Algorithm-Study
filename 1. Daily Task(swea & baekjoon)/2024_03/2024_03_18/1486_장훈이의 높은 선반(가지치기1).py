def backtrack(i, s):
    global min_s
    
    # 기저 조건
    if i == n:
        # 클 때만 갱신
        if s >= b:
            min_s = min(min_s, s)
        return
    
    else:
        # 가지치기
        if s >= min_s:
            min_s = min(min_s, s)
            return
        
        else:
            backtrack(i+1, s) # 더하지 않은 경우
            backtrack(i+1, s + s_lst[i]) # 더한 경우
             

t = int(input())

for tc in range(1,t+1):
    n, b = map(int,input().split())
    s_lst = list(map(int,input().split()))
    
    # dfs 재료
    p = list(range(n))
    min_s = 99999999
    
    backtrack(0, 0)
    
    print(f'#{tc} {min_s-b}')