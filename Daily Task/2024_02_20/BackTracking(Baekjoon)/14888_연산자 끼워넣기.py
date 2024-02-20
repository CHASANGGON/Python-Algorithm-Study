# 피곤해서 머리가 안 돌아가효...
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
# + - × /
op_num = list(map(int,input().split()))
op_dict = {0:'+', 1:'-', 2:'*', 3:'/'}
op = ''
for i in range(4):
    op += op_num[i]*op_dict[i]
print(op)

stack = []
# for i in range()
# gg....