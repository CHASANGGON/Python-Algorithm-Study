def f(i, w, v):
    global max_v
    
    if w > k:
        return
    else:
        if v > max_v:
            max_v = v

        if w == k:
            print(max_v)
            exit()
        else:
            for j in range(i,n):
                f(j+1, w+wv_lst[j][0], v+wv_lst[j][1])


import sys
input = sys.stdin.readline

n, k = map(int,input().split())

wv_lst = []
for _ in range(n):
    w, v = map(int,input().split())
    wv_lst.append([w,v])

wv_lst.sort(key = lambda x : x[1]/x[0], reverse=True)
max_v = 0
f(0, 0, 0)
print(max_v)