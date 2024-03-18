n = int(input())
lst = '369'

for i in range(1,n+1):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        cnt = 0
        for c in '369':
            cnt += str(i).count(c)
        i = '-'*cnt

    print(i,end=' ')