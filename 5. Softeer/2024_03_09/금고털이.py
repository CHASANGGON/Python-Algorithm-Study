import sys
input = sys.stdin.readline

# 입력 1
w, n = map(int,input().split())

# 입력 2
mp = []
for _ in range(n):
    m, p = map(int,input().split())
    mp.append([m,p])

mp.sort(key = lambda x : (x[1]), reverse=True)

i = 0
result = 0
while 1:
    if w - mp[i][0] > 0:
        w -= mp[i][0]
        result += mp[i][0]*mp[i][1]
    else:
        result += w*mp[i][1]
        break
    i += 1
    
print(result)