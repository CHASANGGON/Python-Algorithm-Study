import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

def seires(depth):
    if depth == m:
        print(*lst)
    else:
        for num in arr:
            if lst:
                if num >= lst[-1]:
                    lst.append(num)
                    seires(depth+1)
                    lst.pop()
            else:
                lst.append(num)
                seires(depth+1)
                lst.pop()
lst = []
seires(0)