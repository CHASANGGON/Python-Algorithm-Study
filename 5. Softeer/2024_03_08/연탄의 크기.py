import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))

mx = 0

for i in range(2,max(arr)+1):
    cnt = 0
    for j in range(n):
        if arr[j] % i == 0:
            cnt += 1
    mx = max(mx, cnt)
    
print(mx)