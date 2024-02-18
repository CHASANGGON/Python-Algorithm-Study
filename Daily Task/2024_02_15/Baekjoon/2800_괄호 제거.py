import sys
input = sys.stdin.readline

# 먼저 valid 한지 체크
# valid 하다면, 
# valid한 괄호쌍이 n개면 2^n - 1 개가 나옴
# 사전 순 출력은 sort를 하면 됨

string = input.rstrip()

stack = []
for s in string:
    if s == '(':
        stack.append(s)
    elif s == ')' and stack and stack[-1] == '(':
        stack.pop()
    else: