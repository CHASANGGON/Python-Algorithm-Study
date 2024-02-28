import sys
input = sys.stdin.readline

n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

arr.sort(key = lambda x : (x[1], x[0]))

stack = [arr[0]]
cnt = 0
for i in range(1,n):
    if arr[i][0] >= stack[-1][1]:
        stack.append(arr[i])
        cnt += 1

print(cnt)