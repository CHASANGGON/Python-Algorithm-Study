import sys
input = sys.stdin.readline

arr = [list(map(int,input().split())) for _ in range(3)]
mn = 999


for i in range(3):
    a = []
    b = []
    for j in range(3):
        a.append(arr[i][j])
        b.append(arr[j][i])
    a.sort()
    b.sort()
    c = 0
    d = 0
    for j in range(3):
        c += abs(arr[i][j]-a[1])
        d += abs(arr[j][i]-b[1])
    mn = min(mn, c, d)
    
print(mn)