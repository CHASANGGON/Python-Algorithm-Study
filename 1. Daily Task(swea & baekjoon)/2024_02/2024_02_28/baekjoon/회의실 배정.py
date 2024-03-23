import sys
input = sys.stdin.readline

n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

arr.sort(key = lambda x : (x[1], x[0]))

stack = [arr[0]]
for i in range(1,n):
    # 이 전 회의 끝나는 시간 <= 새로운 회의 시작 시간
    if stack[-1][1] <= arr[i][0]:
        stack.append(arr[i])

print(len(stack))