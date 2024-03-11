import sys
input = sys.stdin.readline

n = int(input())

course = []
for _ in range(n):
    course.append(list(map(int,input().split())))
    
course.sort(key = lambda x : (x[1], x[0]))

cnt = 1
last_end_time = course[0][1] # 마지막 강의 끝나는 시간
for i in range(1,n):
    if last_end_time <= course[i][0]:
        last_end_time = course[i][1] # 끝나는 시간 갱신
        cnt += 1 # 카운트
        
print(cnt)