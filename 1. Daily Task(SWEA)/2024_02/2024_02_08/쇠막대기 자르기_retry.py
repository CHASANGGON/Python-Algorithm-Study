T = int(input())
for test_case in range(1,T+1):
    parenthesis = input()

    cnt = 0
    stack = []
    for p in parenthesis:
        
        # (
        if p == '(':
            stack.append(p)

        # )
        else:
            # whether 레이저 or 쇠막대 -> pop
            stack.pop()
            
            # 레이저
            if before == '(':
                cnt += len(stack)
            # 쇠막대의 끝
            else:
                cnt += 1
        before = p

    print(f'#{test_case} {cnt}')