t = int(input())

for tc in range(1,t+1):

    n, k = map(int,input().split())

    string = input()

    nums = []

    for _ in range(n//4):
        for i in range(4):
            nums.append(string[i*(n//4):(i+1)*(n//4)])
        string = string[1:] + string[0]

    nums.sort()

    nums = list(set(nums))

    print(f'#{tc} {int(nums[-k], 16)}')