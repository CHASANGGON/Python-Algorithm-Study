import sys
input = sys.stdin.readline

n = int(input())

arr = [0]*n
cnt = [0](n+1)

for i in range(n):
    arr[i] = int(input())
    
    
arr.sort()

s = sum(arr)

print(s/n)
print(arr[n//2])
print()