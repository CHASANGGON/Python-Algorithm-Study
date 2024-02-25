# 기타 줄은 (1~6번 줄) * (P개 프렛) 
# (어떤 줄의) 프렛을 누르면 가장 높은 프렛의 음이 발생
# 5 & 7 -> 7
# 2 & 5 & 7 -> 2를 발생시키려면 5 & 7 을 제거

# 마치 오름차순으로 저장되는 스택과 동일하다!!
# 다만 특이한 것은 줄이 여러 개 라는 것이다.
# 그래서 스택을 여러 개 만들고, 스택 하나당 하나의 줄이라 생각!

# 그 후 손가락으로 프렛을 누르거나(PUSH) 떼는 것(POP)을
# 손가락을 한 번 움직였다고 하니까 PUSH & POP을 COUNT

import sys
input = sys.stdin.readline

n, p = map(int,input().split())
stack = [[] for _ in range(7)]

# n번의 입력
cnt = 0
for _ in range(n):
    line, flat = map(int,input().split())
    # 출력하고자 하는 음의 프렛이 더 높다면 push & count
    if stack[line] and stack[line][-1] < flat:
        stack[line].append(flat)
        cnt += 1
    
    # 출력하고자 하는 음의 프렛이 더 낮다면 pop & count
    elif stack[line] and stack[line][-1] > flat:
        # top의 프렛이 나보다 작아질 때까지
        while stack[line] and stack[line][-1] > flat:
            stack[line].pop()
            cnt += 1
        # 이 때 top의 프렛이 나와 같지 않고
        # 나보다 작아야만 push & count
        # 같으면 그냥 바로 음을 발생시키면 되므로
        # count를 하지 않는다.
        if stack[line] and stack[line][-1] < flat:
            stack[line].append(flat)
            cnt += 1
        elif not stack[line]:
            stack[line].append(flat)
            cnt += 1
            
            
    # 스택이 비었으면(프렛이 아무것도 안 눌렸으면) push & count
    # 굳이 not stack이라고 명시한 이유는
    # 발생시키려는 프렛의 높이와
    # 스택안의 프렛의 높이가 동일 할 때도 count될 수 있기 때문에
    elif not stack[line]:
        stack[line].append(flat)
        cnt += 1

print(cnt)