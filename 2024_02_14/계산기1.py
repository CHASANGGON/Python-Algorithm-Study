T = 10
for test_case in range(1,T+1):
    n = int(input())
    formular = input()
    stack = []

    # 1. 후위 표기식으로 바꾸기
    postfix = ''
    for f in formular:
        if f.isdigit():
            postfix += f
        elif not stack:
            stack.append(f)
        else:
            postfix += stack.pop()
            stack.append(f)
    # 마지막에 stack에 들어있는 연산자도 추가하기!!
    postfix += stack.pop()
    
    # 2. 후위 표기식 계산하기
    stack = []
    for p in postfix:
        if p.isdigit():
            stack.append(int(p))
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(a+b)

    print(f'#{test_case} {stack[0]}')
        