import math

def calculate_angle(my_ball, target_ball):
    
    # 각도 계산
    width = target_ball[0] - my_ball[0]
    height = target_ball[1] - my_ball[1]
    theta = math.atan2(height, width)
    degree = math.degrees(theta)
    
    # 원점을 기준으로 보정
    angle = 90 - degree    #<<<<<<<<<<<<<<< 사실상 보정 부분은 여기 뿐인듯???
    if angle < 0:          #<<<<<<<<<<<<<<<
        angle += 360       #<<<<<<<<<<<<<<<
    
    return angle

my_ball = (0, 0)
target_balls = [(1, 3), (2, 2), (3, 1), (4, 0), (3, -1), (2, -2), (1, -3), (0, -4), (-1, -3), (-2, -2), (-3, -1), (-4, 0), (-3, 1), (-2, 2), (-1, 3), (0, 4)]
target_ball = (10, 10) # 파워 예시
# c(두 공사이의 간격) = sqrt(a ** 2 + b ** 2)
distance = math.sqrt((target_ball[0] - my_ball[0] ** 2 + (target_ball[1] - my_ball[1]) ** 2))
power = max(10.0, distance * 2) # 0~100 (권장 파워는 10 이상, 100이상넘길수있지만 100으로고정)

for target_ball in target_balls:
    angle = calculate_angle(my_ball, target_ball)
    print(f"Target Ball: {target_ball}, Angle: {angle}")
    print(power)