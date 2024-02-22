def post_traversal_calculate(now_v): # 후위 표기식 계산
    if now_v:
        post_traversal_calculate(left[now_v])
        post_traversal_calculate(right[now_v])

        if value[now_v].isdigit():
            stack.append(int(value[now_v]))
        else:
            b = stack.pop()
            a = stack.pop()
            if value[now_v] == '/':
                stack.append(a//b)
            elif value[now_v] == '*':
                stack.append(a*b)
            elif value[now_v] == '+':
                stack.append(a+b)
            else:
                stack.append(a-b)
   
t = 10

for tc in range(1,1+t):
    n = int(input()) # 입력
    
    left = [0]*(n+1)
    right = [0]*(n+1)
    value = [0]*(n+1) # 값을 담을 리스트 생성
    
    for _ in range(n): # 입력
        a = list(input().split())
        
        if len(a) == 2: # 정수
            v, d = a[0], a[1] # vertex, decimal
            value[int(v)] = d
        else: # 연산자
            v, o, l, r = a[0], a[1], a[2], a[3] # vertex operator left right
            v = int(v)
            left[v] = int(l)
            right[v] = int(r)
            value[v] = o
    
    stack = []
    post_traversal_calculate(1) # 후위표기식 만들기(후위 순회)
    
    print(f'#{tc} {stack[-1]}') # 계산해서 바로 출력