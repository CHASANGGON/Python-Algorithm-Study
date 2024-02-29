import sys
input = sys.stdin.readline

n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

# 끝나는 시간 기준 1차 정렬
# 시작 시간 기준 2차 정렬
arr.sort(key = lambda x : (x[2], x[1], x[0]))

s = arr[0][2]
stack = [arr[0]]

for i in range(1,n):
    if stack[-1][1] <= arr[i][0]:
        stack.append(arr[i])
        s += arr[i][2]
        
print(s)