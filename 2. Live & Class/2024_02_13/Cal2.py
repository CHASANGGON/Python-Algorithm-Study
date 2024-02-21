# 계산기2 (후위식 -> 계산하여 결과)
postfix = "113+4*5/+"
stack = []  # 스택

for ch in postfix:
    # 피연산자(숫자)를 스택에 넣겠다...
    if ch.isdigit():
        stack.append(ch)

    # 연산자를 만나면 피연산자를 두개 빼서 연산...! stack에 push...
    else:  # 연산자 * / + -
        b = int(stack.pop())
        a = int(stack.pop())
        if ch == '*':
            stack.append(a * b)
        elif ch == '/':
            stack.append(a // b)
        elif ch == '+':
            stack.append(a + b)
        elif ch == '-':
            stack.append(a - b)

# 순회가 완료되면 스택에 단 하나의 결괏값이 남게 된다...
result = stack.pop()
print(result)