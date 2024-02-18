def f(i,k):
    
    # 기저 조건
    if i == k:
        print(*P)
        
    # 문제의 부분
    # 값을 교환해서 재귀호출을 하는 부분
    else:
        for j in range(i,k):
            P[i], P[j] = P[j], P[i] # 값을 교환
            f(i+1, k)
            P[i], P[j] = P[j], P[i] # 복구

P = [1,2,3]
f(0,3)