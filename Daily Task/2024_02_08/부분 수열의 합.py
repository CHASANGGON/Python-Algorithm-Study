T = int(input())

for test_case in range(1,T+1):
    n, k = map(int,input().split())
    series = list(map(int,input().split()))

    cnt = 0
    for i in range(1<<n): # 1<<n : 1을 n비트 밀면 2^n -> range(1<<n) : n = 4 -> range(16) : 0000~1111 (0~15) 범위의 2진수에 해당 
        series_sum = 0 # 매 case 마다 합을 저장할 변수
        for j in range(n):
            if i & (1<<j):
                series_sum += series[j] # 누적합
        if series_sum == k: # 비교
            cnt += 1
    
    print(f'#{test_case} {cnt}')

# 부분 수열의 합도 부분 집합과 마찬가지로
# 각 요소가 있는지 or 없는지의 경우를 모두 나열했는 것과 동일하므로
# 부분집합 공식을 활용해서 해당하는 수열들을 모두 구하는 과정에서
# 각 수열의 요소들의 합이 주어진 값과 일치하는지를 따지면 됩니다.