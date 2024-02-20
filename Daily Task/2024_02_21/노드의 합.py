T = int(input())

for test_case in range(1,T+1):
    n, m, l = map(int,input().split())

    arr = [0]*(n+2)
    for _ in range(m):
        N, V = map(int,input().split())
        arr[N] = V
    
    # 끝에서부터 n//2 번만 더하면 됨
    for i in range(n//2,0,-1):
        arr[i] = arr[i*2] + arr[i*2+1]
    
    print(f'#{test_case} {arr[l]}')