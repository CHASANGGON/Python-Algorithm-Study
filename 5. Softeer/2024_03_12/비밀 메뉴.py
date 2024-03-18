def check():
    for i in range(n-m+1):
        if key == inp[i:i+m]:
            print('secret')
            return
    print('normal')

import sys
input = sys.stdin.readline

m,n,k = map(int,input().split())

key = list(map(int,input().split()))
inp = list(map(int,input().split()))

check()