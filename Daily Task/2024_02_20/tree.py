'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def pre_order(T):
    if T:
        print(T, end =' ')
        pre_order(left[T])
        pre_order(right[T])


N = int(input()) # 1번부터 N번까지인 정점
E = N - 1
arr = list(map(int,input().split()))
left = [0]*(N+1)
right = [0]*(N+1)
par = [0]*(N+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]

    # 그냥 왼쪽부터 채우는 거 ㅇㅇ..
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c
    par[c] = p

c = N
while par[c] != 0: # 부모가 있으면
    c = par[c]     # 부모를 새로운 자식으로 두고
root = c
print(root)
pre_order(root)