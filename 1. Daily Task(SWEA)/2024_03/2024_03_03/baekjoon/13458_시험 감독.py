# N개의 시험장
# i번 시험장에 있는 응시자의 수는 Ai명
# 총감독관은 한 시험장에서 감시할 수 있는 응시자의 수가 B명
# 부감독관은 한 시험장에서 감시할 수 있는 응시자의 수가 C명
# 시험장에 총감독관은 오직 1명만 있어야 하고
# 부감독관은 여러 명 있어도 됨
# 응시생들을 모두 감시
# 필요한 감독관 수의 최솟값
import sys
sys.stdin.readline

# N
N = int(input())

# Ai
A = list(map(int,input().split()))

# B C
B, C = map(int,input().split())

s = 0

for i in range(N):
    s += 1
    if A[i]-B > 0:
        s += (A[i]-B)//C
        remain = (A[i]-B)%C
        if remain > 0 :
            s += 1
    
print(s)