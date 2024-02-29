import sys
input = sys.stdin.readline
parenthesis = input().rstrip()

cnt = 0
stack = []
for p in parenthesis:
    
    if p == '(':
        stack.append(p)
    else:
        stack.pop()
        if before == '(':
            cnt += len(stack)
        else:
            cnt += 1
    before = p
print(cnt)