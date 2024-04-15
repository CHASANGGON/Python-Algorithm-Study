import sys
input = sys.stdin.readline

# 채점현황들 보니까 이렇게 만들어놓고 쓰는 거 보다 비트 마스킹이 더 빠른 듯..
nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 
        2048, 4096, 8192, 16384, 32768, 65536, 131072, 
        262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216]
n, k = map(int, input().split()) # 입력

if n <= k: # 합칠 필요 없이 바로 가져가면 되는 경우
    print(0)
else: # 합쳐야 하는 경우
    
    # 합칠 수 있는 병이 한 개만 남았거나(k == 1)
    # 이미 모든 물병들을 나눠 담았다면 stop!(n == 0)
    while k > 1 and n:
        
        before = 1 # 만들어야 하는 크기가 1이면 바로 종료 -> before 미리 생성해줘야함
        for num in nums:
            if n <= num: # 현재 n = 5 라고 생각한다면  ->  5 < 8(2의 3승)에서 stop
                break
            else:
                before = num # before에는 4(2의 2승)가 저장 돼 있음
        n -= before
        # 그러면 합치기만 하면 바로 만들 수 있다는 뜻이므로 
        # before의 크기 만큼 n에서 빼주기
        k -= 1 # 병 수도 카운트
        
    if n: # 그렇게 했는데도 아직 물이 남아있다면 -> 물을 사와야한다!
        for num in nums:
                if n <= num:
                    print(num - n) # 제일 가까운 2의 n승이 될 수 있을 만큼 사오면 된다! -> 바로 출력
                    break

    else: # 남은 물이 없다면
        print(0) # 물을 사지 않아도 된다!