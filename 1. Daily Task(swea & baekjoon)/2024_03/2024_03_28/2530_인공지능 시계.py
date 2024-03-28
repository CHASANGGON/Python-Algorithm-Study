import sys
input = sys.stdin.readline

a, b, c = map(int, input().split()) 
d = int(input())

total = a * 3600 + b * 60 + c + d

a = total // 3600
total%=3600
b = total // 60
total%=60
c = total

print(a%24, b%60, c%60)