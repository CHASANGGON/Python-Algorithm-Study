def backtrack(i, s):
    global min_s
     
    # 한 번 min_s가 설정되고나면 가치지기
    if s >= min_s:
        return
     
    # 기저 조건
    # 처음 min_s 를 결정하기 위해 설정필요
    if i == n:
        if s >= b:
            min_s = min(min_s, s)
        return
         
    backtrack(i+1, s + s_lst[i]) # 더한 경우
    backtrack(i+1, s) # 더하지 않은 경우
              
 
t = int(input())
 
for tc in range(1,t+1):
    n, b = map(int,input().split())
    s_lst = list(map(int,input().split()))
     
    # dfs 재료
    p = list(range(n))
    min_s = 99999999
     
    backtrack(0, 0)
     
    print(f'#{tc} {min_s-b}')