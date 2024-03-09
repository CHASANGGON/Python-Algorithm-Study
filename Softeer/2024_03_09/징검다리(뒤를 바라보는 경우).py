import sys
input = sys.stdin.readline

n = int(input())


arr = list(map(int,input().split()))
ans = [1]*n

for i in range(n-1):
    for j in range(i+1,n):
        if arr[i] < arr[j]:
            ans[j] = max(ans[j], ans[i]+1)

# 어디서 출발하든 어디서 도착하든 상관없음..
print(max(ans))