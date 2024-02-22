# 10진수 -> N진수
def convert(num, N):
    dic = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9',
        10:'A', 11:'B', 12:'C', 13:'D', 14:'E' , 15:'F'}
    remains = [] # 나머지들
    while num != 0:
        # 몫과 나머지를 구하는 과정
        num, r  = num // N, num % N
        # 나머지는 remains 리스트에 저장
        remains.append(dic[r])
    
    return remains[::-1]

print(''.join(convert(254, 16)))