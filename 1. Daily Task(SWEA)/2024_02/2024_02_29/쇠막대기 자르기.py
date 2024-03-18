t = int(input())

for tc in range(1,t+1):
    parenthesis = input()

    stack = []
    result = 0

    for p in parenthesis:
        if p == '(':
            stack.append(p)
            before = p
        # 레이저
        elif before == '(':
            stack.pop()
            result += len(stack)
            before = p
        # 쇠막대 끝
        else:
            stack.pop()
            result += 1
            before = p

    print(f'#{tc} {result}') 