t = int(input())

for tc in range(1,t+1):
    string = input()
    
    stack = []
    for s in string:
        # 스택의 top 요소가 삽입하려는 요소와 동일하면 pop(삭제)
        if stack and stack[-1] == s:
            stack.pop()
        # 동일하지 않으면 push
        else:
            stack.append(s)
            
    print(f'#{tc} {len(stack)}')