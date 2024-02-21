import sys
input = sys.stdin.readline

parenthesis = input().rstrip()

result = 0
stack = []
score_chart = {'(':2, ')':2, '[':3, ']':3}
for p in parenthesis:
    
    if p in '([':
        stack.append(p)
        left_check = True
        
    elif p == ')' and stack and stack[-1] == '(':
        if left_check:
            multiple = 1
            if stack:
                for s in stack:
                    multiple *= score_chart[s]
            result += multiple
        left_check = False
        stack.pop()
        
    elif p == ']' and stack and stack[-1] == '[':
        if left_check:
            multiple = 1
            if stack:
                for s in stack:
                    multiple *= score_chart[s]
            result += multiple
        left_check = False
        stack.pop()
    else:
        stack.append(p)
if stack:
    print(0)
else:
    print(result)