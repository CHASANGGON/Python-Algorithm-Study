t = 10

for tc in range(1,t+1):
    input()
    table = [input().split() for _ in range(100)]
    cnt = 0
    for i in range(100):
        stack = []
        for j in range(100):
            if stack:
                if table[j][i] == '2':
                    stack.pop()
                    cnt += 1
            else:
                if table[j][i] == '1':
                    stack.append(['1'])
    
    print(f'#{tc} {cnt}')