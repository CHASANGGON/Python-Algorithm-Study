t = int(input())

for tc in range(1,t+1):
    n = int(input())

    trucks = []

    for _ in range(n):
        trucks.append(list(map(int,input().split())))

    trucks.sort(key = lambda x : (x[1], x[0]))

    cnt = 1
    stack = [trucks[0]]

    for truck in trucks:
        # 새 작업 시작 시간이, 이전의 작업 종료시간보다 늦거나 같을 때
        if truck[0] >= stack[-1][1]:
            stack.append(truck)
            cnt += 1
    
    print(f'#{tc} {cnt}')