def find_start():
    l, r, s = 0, 0, 0
    while s < S:
        s += arr[r]
        r += 1
    return [l, r, s]
    
import sys
input = sys.stdin.readline

N, S = map(int,input().split())
arr = list(map(int,input().split()))

if S in arr:
    print(1)
else:
    # 처음 위치 찾기
    l, r, s = find_start()
    min_lr = r - l 
    s += -arr[l]
    l += 1

    while r < N and l != r:
        if s < S:
            s += -arr[l] + arr[r]
            l += 1
            r += 1
        elif s >= S:
            min_lr = r - l + 1
            s += -arr[l]
            l += 1
        
    print(min_lr)   