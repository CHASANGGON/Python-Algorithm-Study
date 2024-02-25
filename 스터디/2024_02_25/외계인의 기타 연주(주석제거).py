import sys
input = sys.stdin.readline

n, p = map(int,input().split())
stack = [[] for _ in range(7)]


cnt = 0
for _ in range(n):
    line, flat = map(int,input().split())

    if stack[line] and stack[line][-1] < flat:
        stack[line].append(flat)
        cnt += 1
    
    elif stack[line] and stack[line][-1] > flat:
        while stack[line] and stack[line][-1] > flat:
            stack[line].pop()
            cnt += 1
        if stack[line] and stack[line][-1] < flat:
            stack[line].append(flat)
            cnt += 1
        elif not stack[line]:
            stack[line].append(flat)
            cnt += 1
            
    elif not stack[line]:
        stack[line].append(flat)
        cnt += 1

print(cnt)