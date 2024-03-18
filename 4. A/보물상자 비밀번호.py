T = int(input())

for test_case in range(1,T+1):
    N, K = map(int,input().split())

    treasure_chest = input()

    nums = []

    for _ in range(N//4): # 회전 수
        for j in range(4): # 4등분
            nums.append(treasure_chest[j*(N//4):(j+1)*(N//4)])
        treasure_chest = treasure_chest[1:] + treasure_chest[0]

    nums = list(set(nums))
    nums.sort()
    print(f'#{test_case} {int(nums[-K],16)}')