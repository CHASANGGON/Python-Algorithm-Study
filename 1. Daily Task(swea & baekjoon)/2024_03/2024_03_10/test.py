T = int(input())

for test_case in range(1,T+1):
    N, M = map(int,input().split())
    
    arr = [list(input()) for _ in range(N)]

    print(f'#{test_case} ',end='')

    # 가로 검증    
    for i in range(N): # N = 13 -> range(13) : 0~12
        for j in range(N-M+1): # range(4) : 0~3
            string = arr[i][j:j+M] # 리스트 슬라이싱
            if string == string[::-1]: # 반전시켜서 비교
                print(''.join(string))
    
    # 전치행렬로 만들기
    arr = list(zip(*arr))

    # 전치행렬로 만든 다음에 다시 한 번 가로 검증    
    for i in range(N): # N = 13 -> range(13) : 0~12
        for j in range(N-M+1): # range(4) : 0~3
            string = arr[i][j:j+M] # 리스트 슬라이싱
            if string == string[::-1]: # 반전시켜서 비교
                print(''.join(string))