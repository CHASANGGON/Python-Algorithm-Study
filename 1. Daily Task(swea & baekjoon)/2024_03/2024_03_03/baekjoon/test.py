import sys
sys.stdin.readline

n = int(input())

x_lst = [0]*101
y_lst = [0]*101
x_y_lst = [0]*101
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x,x+10):
        x_lst[i] = 1
    for i in range(y,y+10):
        y_lst[i] = 1
        
for i in range(1,101):
    if x_lst[i] ^ y_lst[i]:
        x_y_lst[i] = 1

print((x_lst.count(1)+y_lst.count(1))*2+x_y_lst.count(1)*4)
    