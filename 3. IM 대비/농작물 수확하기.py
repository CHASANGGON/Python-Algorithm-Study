
        

t = int(input())

for tc in range(1,1+t):
    n = int(input())
    
    farm = [list(map(int,list(input()))) for _ in range(n)]
    
    for i in range(n//2):
        