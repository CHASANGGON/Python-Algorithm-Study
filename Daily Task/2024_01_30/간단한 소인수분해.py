T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    divisior = [2, 3, 5, 7, 11]
    counts = [0]*5
    
    for i in range(5):
        while n % divisior[i] == 0:
            n //= divisior[i]
            counts[i] += 1
    
    print(f'#{test_case} ', end='')
    print(*counts)