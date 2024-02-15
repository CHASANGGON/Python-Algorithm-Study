T = int(input())

for test_case in range(1,1+T):
    N, M = map(int,input().split()) # 가로 세로
    
    national_flag = [input() for _ in range(N)]
    print(national_flag)