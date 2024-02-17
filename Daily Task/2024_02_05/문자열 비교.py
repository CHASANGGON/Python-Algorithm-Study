T = int(input())

for test_case in range(1,T+1):
    word1 = input()
    word2 = input()
    print(f'#{test_case} ',end='')
    if word1 in word2:
        print(1)
    else:
        print(0)