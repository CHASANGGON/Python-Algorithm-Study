n = int(input())
num = int(input())
arr =[[0]*n for _ in range(n)]
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
i, j, k = 0, 0, 0

n_square = n**2
arr[i][j] = n_square
n_square -= 1
while n_square > 0:
    while 0 <= i+di[k] <= n-1 and 0 <= j+dj[k] <= n-1 and arr[i+di[k]][j+dj[k]] == 0:
        i += di[k]
        j += dj[k]
        arr[i][j] = n_square
        n_square -= 1
    k = (k+1)%4 

for a in arr:
    print(*a)

for i in range(n):
    if num in arr[i]:
        for j in range(n):
            if num == arr[i][j]:
                print(i+1,j+1)

