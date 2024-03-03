import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

stack = [arr[-1]] # 내림차순을 유지
result = [-1] # 출력

arr = arr[::-1]

for a in arr[1:]:
    
    # 큰 수가 있으면 내림차순 유지 가능 -> push
    if stack[-1] > a:
        result.append(stack[-1])
        stack.append(a)
    
    # 큰 수가 나올 때까지
    else:
        # pop
        while stack and stack[-1] <= a:
            stack.pop()
        
        # stack이 비었다면 큰 수를 못 찾은 경우
        if not stack:
            result.append(-1)
        
        # 큰 수를 찾았으면 큰수를 출력에 추가
        else:
            result.append(stack[-1])

        # 큰 수 다음으로 본인을 push -> 내림차순 유지
        stack.append(a)
            
print(*result[::-1])