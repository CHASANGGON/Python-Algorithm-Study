import sys
input = sys.stdin.readline

n = int(input())


arr = list(map(int,input().split()))
ans = [1]*n

for i in range(1,n):
    for j in range(i):
        if arr[j] < arr[i] and ans[j]+1 > ans[i]:
            ans[i] = ans[j] + 1
            
print(max(ans))