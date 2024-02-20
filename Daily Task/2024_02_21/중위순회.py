# in_order = Left Vertex Right
def in_order(now_v):
    if now_v:
        in_order(left[now_v])  # L
        print(value[now_v],end='')
        in_order(right[now_v]) # R

T = 10
for test_case in range(1,T+1):
    n = int(input())
    
    left = [0]*(n+1)
    right = [0]*(n+1)
    value = [0]*(n+1)
    
    for i in range(n):
        # 2 F 4 5
        info = [0]*4
        info = list(input().split())
        l = len(info)
        if l >= 3:
            left[int(info[0])] = int(info[2])
        if l == 4:
            right[int(info[0])] = int(info[3])
        value[int(info[0])] = info[1]

    # 루트 정점의 번호는 항상 1
    root = 1
    print(f'#{test_case} ',end='')
    in_order(root)
    print()