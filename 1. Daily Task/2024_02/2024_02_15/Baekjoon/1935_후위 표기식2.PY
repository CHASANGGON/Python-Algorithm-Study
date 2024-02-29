import sys
input = sys.stdin.readline

n = int(input())
formula = input().rstrip() 
values = [float(input()) for _ in range(n)]

# 수식에 사용될 문자-value 딕셔너리 생성
num_dic = {}
for i in range(n):
    num_dic[chr(65+i)] = values[i]

stack = []
for f in formula:
    if f in '+-*/':
        b = stack.pop()
        a = stack.pop()
        if f == '+':
            stack.append(a+b)
        if f == '-':
            stack.append(a-b)
        if f == '*':
            stack.append(a*b)
        if f == '/':
            stack.append(a/b)
        
    else:
        stack.append(num_dic[f])

print(f'{stack[-1]:.2f}')