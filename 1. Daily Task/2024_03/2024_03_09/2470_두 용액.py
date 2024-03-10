import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr.sort()

# 음수 -> 양수 인덱스 찾기기
for i in range(n):
    if arr[i] > 0:
        break

l_arr = arr[:i]
r_arr = arr[i:]
r_arr = r_arr[::-1]
if l_arr:
    l, r = 0, 0

    dic = {}
    while l != i and i + r != n:
        s = l_arr[l] + r_arr[r]
        if s == 0:
            print(l_arr[l],r_arr[r])
            quit()
        dic[abs(s)] = [l_arr[l],r_arr[r]]
        if s > 0:
            r += 1
        else:
            l += 1
    
    if len(l_arr) >= 2:
        dic[abs(l_arr[-1]+l_arr[-2])] = [l_arr[-2],l_arr[-1]]
    if len(r_arr) >= 2:
        dic[abs(r_arr[-1]+r_arr[-2])] = [r_arr[-1],r_arr[-2]]
    a = list(dic.keys())
    print(*dic[min(a)])
else:
    print(r_arr[-1], r_arr[-2])