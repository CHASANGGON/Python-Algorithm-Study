import sys
input = sys.stdin.readline

parentheis = input().rstrip()

stack = []
for p in parentheis:
    if p == '(':
        stack.append(p)
    else:
        if stack and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(p)

print(len(stack))