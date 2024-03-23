def f():
    print(f'#{test_case} ',end='')
    
    for i in range(N): # row
        for j in range(N): # col
            for k in range(4): # del
                if arr[i][j] == 'o': # judge
                    for l in range(1,6): # lengthening
                        if 0 <= i + l*di[k] < N and 0 <= j + l*dj[k] < N and arr[i+l*di[k]][j+l*dj[k]] == 'o':
                            pass
                        else:
                            break
                    if l == 5: # range(1,5) & if l == 4 로 하면 안 되는 이유 -> 다섯 번째 값이 'o'가 아니라도 l값은 4까지 도달
                        print('YES')
                        return
    print('NO')

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    
    di = [1,0,1,1] # (상)하(좌)우대각선
    dj = [0,1,1,-1]
    f()    