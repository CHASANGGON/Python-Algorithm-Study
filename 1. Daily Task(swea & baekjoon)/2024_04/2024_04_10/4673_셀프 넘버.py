import sys
input = sys.stdin.readline

answer = [1] * 10001
for num in range(1,10001):
    if answer[num]:
        while True:
            num_copy = num
            for n in str(num_copy):
                num += int(n)
            if num > 10000:
                break
            answer[num] = 0
            
for i in range(1,10001):
    if answer[i]:
        print(i)