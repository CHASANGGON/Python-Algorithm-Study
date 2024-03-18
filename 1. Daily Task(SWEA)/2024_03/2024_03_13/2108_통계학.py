import sys
input = sys.stdin.readline

n = int(input())

cnt = [0]*(8001)
for _ in range(n):
    cnt[int(input())+4000] += 1
    
idx = 0
arr = [0]*n
max_freq = 1
for i in range(8001):
    if cnt[i]:
        if cnt[i] > max_freq:
            max_freq = cnt[i]
        for _ in range(cnt[i]):
            arr[idx] = i-4000
            idx += 1

max_freq_num = cnt.index(max_freq) - 4000
if cnt.count(max_freq) >= 2:
    first_max_idx = cnt.index(max_freq)
    max_freq_num = cnt[first_max_idx+1:].index(max_freq) - 4000 + first_max_idx + 1

print(round(sum(arr)/n))
print(arr[n//2])
print(max_freq_num)
print(max(arr)-min(arr))