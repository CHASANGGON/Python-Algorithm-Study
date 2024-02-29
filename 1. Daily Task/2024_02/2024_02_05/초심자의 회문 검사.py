T = int(input())

for test_case in range(1,T+1):
    word = input()
    print(f'#{test_case} ',end='')
    if word == word[::-1]:
        print(1)
    else:
        print(0)