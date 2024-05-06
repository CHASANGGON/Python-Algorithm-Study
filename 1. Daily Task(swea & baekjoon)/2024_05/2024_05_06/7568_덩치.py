import sys
input = sys.stdin.readline

n = int(input())

lst = []
for _ in range(n):
    lst.append(list(map(int,input().split())))

for i in range(n):
    cnt = 0
    for j in range(n):
        if i == j:
            continue
        
        if lst[j][0] > lst[i][0] and lst[j][1] > lst[i][1]:
            cnt += 1

    print(cnt+1, end =' ')