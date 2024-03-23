def transpose():
    return list(zip(*arr))

def vertical_calc(arr):
    cnt = 0
    for i in range(101):
        for j in range(100):
            if arr[i][j] != arr[i][j+1]:
                cnt += 1
    return cnt

import sys
sys.stdin.readline

n = int(input())

arr = [[0]*101 for _ in range(101)]

for _ in range(n):
    sj, si = map(int,input().split())
    for i in range(si,si+10):
        for j in range(sj,sj+10):
            arr[i][j] = 1


arr_t = transpose()
print(vertical_calc(arr)+vertical_calc(arr_t))