def preorder(v):
    if v != '.':
        print(v,end='')
        preorder(dic[v][0])
        preorder(dic[v][1])

def inorder(v):
    if v != '.':
        inorder(dic[v][0])
        print(v,end='')
        inorder(dic[v][1])

def postorder(v):
    if v != '.':
        postorder(dic[v][0])
        postorder(dic[v][1])
        print(v,end='')

import sys
input = sys.stdin.readline

n = int(input())

dic = {}

for _ in range(n):
    v, l, r = input().rstrip().split()
    dic[v] = [l,r]

preorder('A')
print()
inorder('A')
print()
postorder('A')