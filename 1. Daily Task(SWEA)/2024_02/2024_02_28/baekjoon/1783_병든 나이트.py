import sys
input = sys.stdin.readline

i, j = map(int,input().split())

if i == 1 or j == 1:
    print(1)
    
elif i == 2:
    # result = (j+1)//2
    # if result > 4:
    #     result = 4    
    # print(result)
    print(min(4,(j+1)//2))

elif i >= 3 and j < 7: # i에 대한 조건은 없어도 된다네~
    # result = j
    # if result > 4:
    #     result = 4
    # print(result)
    print(min(4,j))
    
elif i >= 3 and j >= 7: # i에 대한 조건은 없어도 된다네~
    print(j-2)