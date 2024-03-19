# 중위식 -> 후위식 (스택)

text = "(1+(1+3)*4/5)"
stack = []  # push: append(x) / pop: pop()
result = ''  # 후위식을 넣을 result 변수
# 스택의 상태가 항상 내가 넣으려고 하는 연산자가,
# 기존에 있었던 연산자보다 우선순위가 높도록 유지!
# 중위식을 순회하며 후위식 만들어야 한다..
for ch in text:
    # 1. 숫자(피연산자)가 나오면 그대로 출력
    if ch.isdigit():
        result += ch
    # 2. ( 여는괄호가 나오면
    elif ch == '(':
        # ( 여는괄호를 스택에 push 한다
        stack.append('(')
    # 3. * / 나오면
    elif ch == '*' or ch == '/':
        # 스택에 들어있는 값이 * / 연산자라면 빼준다..
        if len(stack) > 0 and (stack[-1] == '*' or stack[-1] == '/'):
            result += stack.pop()
        stack.append(ch)
    # 4. + - 나오면
    elif ch == '+' or ch == '-':
        # 여는 괄호가 나오거나 스택이 아예 비거나일 경우까지
        # pop 계속 진행해준다...
        while len(stack) > 0 and stack[-1] != '(':
            result += stack.pop()
        stack.append(ch)
    # 5. ) 닫는괄호가 나오면
    elif ch == ')':
        # ( 여는 괄호가 나올 때까지 pop해줘라...!
        while stack[-1] != '(':
            result += stack.pop()
        stack.pop()  # '('

# 순회가 끝난 후, stack 의 내용을 모두 pop해준다...
while len(stack) > 0:
    result += stack.pop()

print(result)