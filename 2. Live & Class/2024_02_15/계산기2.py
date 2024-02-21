import sys

# sys.stdin = open('input.txt', 'r')

# 테스트케이스 수 T
T = 10
for tc in range(1, T + 1):
    # 입력
    # 문자열 길이 N
    N = int(input())
    # 문자열 계산식
    infix = input().rstrip()

    # 로직
    # 중위식 -> 후위식 표현 변경...
    # + 연산자..
    stack = []
    postfix = ''  # 후위식
    # 중위식 -> 후위식으로 순회하며 변경..
    for ch in infix:
        # 숫자(피연산자)
        if ch.isdigit():
            postfix += ch
        # *연산(연산자)
        elif ch == '*':
            while len(stack) > 0 and stack[-1] == '*':
                postfix += stack.pop()
            stack.append(ch)
        # +연산(연산자)
        elif ch == '+':
            # 연산우선순위가 같거나 높은값은 스택 바로 위의 요소는 빼내줘야함...!
            while len(stack) > 0:
                postfix += stack.pop()
            # 연산자는 stack push...!
            stack.append(ch)
    # 스택에 남아있는 연산자들을 모두 후위식에다가 추가...
    while len(stack) > 0:
        postfix += stack.pop()
    
    print(postfix)
    
    # 후위표현식을... 계산을 실시...!
    stack = []
    # 후위표현식을 순회하며...
    for ch in postfix:
        # 스택에다가 피연산자를 넣겠다..
        if ch.isdigit():
            stack.append(ch)
        # 연산자가 나올 때마다...
        elif ch == '*':
            # 숫자를 2개 꺼내 연산을 하고, 다시 스택에 넣겠다...!
            b = int(stack.pop())
            a = int(stack.pop())
            temp = a * b
            stack.append(temp)
        elif ch == '+':
            # 숫자를 2개 꺼내 연산을 하고, 다시 스택에 넣겠다...!
            b = int(stack.pop())
            a = int(stack.pop())
            temp = a + b
            stack.append(temp)

    # 스택에 단 하나의 결과를 꺼내어 출력한다..!
    result = stack.pop()
    # 출력
    print(f"#{tc} {result}")