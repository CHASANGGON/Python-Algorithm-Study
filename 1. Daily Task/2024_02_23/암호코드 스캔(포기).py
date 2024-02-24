t = int(input())

for tc in range(1,t+1):
    n, m = map(int,input().split())
    
    hexa_bit = [input() for _ in range(n)]
    
    # 암호코드 수집
    hexa_pw_dict = {}
    for i in range(n):
        # 암호의 시작점 찾기
        if not hexa_bit[i].isdigit():
            s = 0
            while hexa_bit[i][s] == '0':
                s += 1
            
            e = m - 1
            while hexa_bit[i][e] == '0':
                e -= 1
            
            if s-8 < 0:
                s = 0
            else:
                s -= 8
            hexa_pw_dict[hexa_bit[i][s:e+1]] = 0
    # 암호코드 변환(16 -> 2)
    decrypt_list = ['0000','0001','0010','0011','0100','0101','0110','0111',
     '1000','1001','1010','1011','1100','1101','1110','1111']
    bi_pw_dict = {}
    for hp in hexa_pw_dict.keys():
        # 16 -> 2
        bi_pw = ''
        for h in hp:
            if h.isdigit():
                bi_pw += decrypt_list[ord(h)-48]
            else:
                bi_pw += decrypt_list[ord(h)-55]
        length_control = len(bi_pw)//56

        # 암호의 끝 지점 찾기
        i = len(bi_pw) - 1
        while bi_pw[i] == '0':
            i -= 1
        # 찾은 위치에 맞게 슬라이싱
        a = (i+1)-length_control*56
        if a < 0:
            a = 0
        bi_pw_dict[bi_pw[a:i+1]] = length_control
    
    # 암호의 길이를 고려하여 재생성
    length_56_bi = []
    for bp in bi_pw_dict.keys():
        bi_56 = ''
        interval = bi_pw_dict[bp]
        for i in range(0, 56*interval, interval):
            bi_56 += bp[i]
        length_56_bi.append(bi_56)
    
    
    # 암호 해독
    decrypt_dict = {'0001101':0, '0011001':1, '0010011':2,
                    '0111101':3, '0100011':4, '0110001':5,
                    '0101111':6, '0111011':7, '0110111':8,
                    '0001011':9}
    sum_of_pw = 0
    for l5b in length_56_bi:
        s = 0
        is_valid = 0
        for i in range(8):
            p = decrypt_dict[l5b[i*7:(i+1)*7]]
            s += p
            if i % 2:
                is_valid += p
            else:
                is_valid += p * 3
                
        if is_valid % 10 == 0:
            sum_of_pw += s
    
    print(f'#{tc} {sum_of_pw}')