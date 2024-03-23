import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
x = int(input())

arr.sort()

cnt = 0

for i in range(n-1):
    for j in range(i+1,n):
        if arr[i] + arr[j] == x:
            cnt += 1
        elif arr[i] + arr[j] > x:
            break
    
print(cnt)