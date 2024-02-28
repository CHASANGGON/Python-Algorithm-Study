def f(n):
    
    cnt = 0

    for i in range(1<<n):
        s = 0
        for j in range(n):
            if i & (1<<j):
                s += nums[j]
        if s == k:
            cnt += 1
    return cnt

t = int(input())

for tc in range(1,t+1):
    n, k = map(int,input().split())

    nums = list(map(int,input().split()))

    print(f'#{tc} {f(n)}')