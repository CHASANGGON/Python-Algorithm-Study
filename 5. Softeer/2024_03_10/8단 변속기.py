def mx():
    print('mixed')

def asc():
    for i in range(1,7):
        if arr[i]+1 != arr[i+1]:
            mx()
            return
    print('ascending')
    
def dsc():
    for i in range(1,7):
        if arr[i]-1 != arr[i+1]:
            mx()
            return
    print('descending')

import sys
input = sys.stdin.readline

arr = list(map(int,input().split()))
if arr[0]+1 == arr[1]:
    asc()    
elif arr[0]-1 == arr[1]:
    dsc()
else:
    mx()