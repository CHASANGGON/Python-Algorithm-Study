T = 10

for test_case in range(1,T+1):

    n = int(input()) # 수식의 길이
    formula = input() # 수식
    
    stack = []
    postfix = '' # 후위 계산식 변수

    # “3+4+5+6+7”
    # "34+5+6+7+"
    # 변환 방법
    # 1. 숫자 : postfix에 추가
    # 2. 연산자
    # 2-1. stack empty : 연산자 push
    # 2-2. stack not empty : pop -> postfix에 추가 / 연산자 -> push

    # 1.후위 계산식으로 변환
    for f in formula:
        
        # 2-1 연산자 & stack empty
        if f == '+' and not stack:
            stack.append(f)
        
        # 2-2 연산자 & stack not empty
        elif f == '+' and stack:
            postfix += stack.pop()
            stack.append(f)
        # 1. 숫자
        else:
            postfix += f

    # 마지막 연산자 pop해서 추가
    postfix += stack.pop()

    # 2. 계산
    # 계산 방법
    # 1. 읽은 값이 숫자면 total_stack에 추가
    # 2. 읽은 값이 연산자면 pop해서 두 수를 저장하고, 더 해서 push

    total_stack = []
    for p in postfix:

        # 2. 읽은 값이 연산자면 pop해서 두 수를 저장하고, 더 해서 push
        if p == '+':
            a = total_stack.pop()
            b = total_stack.pop()
            total_stack.append(a + b)

        # 1. 읽은 값이 숫자면 total_stack에 추가
        else:
            total_stack.append(int(p)) # push할 때 정수형으로 변환하는 거 까먹지 않기!

    total = total_stack[0]

    # 3. 출력
    print(f'#{test_case} {total}')