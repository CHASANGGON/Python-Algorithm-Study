import sys
input = sys.stdin.readline

n = int(input())

nums = []
for _ in range(n):
    string = input().rstrip()
    
    digit = ''
    for s in string:
        if s.isdigit():
            digit += s
        else:
            if digit:
                nums.append(int(digit))
                digit = ''
    if digit:
        nums.append(int(digit))
    
nums.sort()
for n in nums:
    print(n)